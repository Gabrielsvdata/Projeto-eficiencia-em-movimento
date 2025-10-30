# gerar_audio_musical.py — voz neural + trilha com volume e fades
import os, sys, asyncio
import edge_tts
from pydub import AudioSegment

BIN_DIR = r"C:\ffmpeg-8.0-essentials_build\bin"   # pasta com ffmpeg.exe e ffprobe.exe
VOZ_NEURAL = "pt-BR-FranciscaNeural"              # ou "pt-BR-AntonioNeural"

TRILHA_VOLUME_DB = -30   # volume da trilha (dB). Ex.: -10 mais alta, -20 mais baixa
FADE_IN_MS       = 2000  # entrada suave da trilha (ms)
FADE_OUT_MS      = 3000  # saída suave da trilha (ms)
# ===================================

FFMPEG_PATH  = os.path.join(BIN_DIR, "ffmpeg.exe")
FFPROBE_PATH = os.path.join(BIN_DIR, "ffprobe.exe")

if not os.path.isfile(FFMPEG_PATH) or not os.path.isfile(FFPROBE_PATH):
    print("❌ ffmpeg/ffprobe não encontrados em:", BIN_DIR)
    sys.exit(1)

# torna ffmpeg/ffprobe visíveis para o processo e para o pydub
os.environ["PATH"] = BIN_DIR + os.pathsep + os.environ.get("PATH", "")
os.environ["FFMPEG_BINARY"]  = FFMPEG_PATH
os.environ["FFPROBE_BINARY"] = FFPROBE_PATH
AudioSegment.converter = FFMPEG_PATH
AudioSegment.ffmpeg    = FFMPEG_PATH
AudioSegment.ffprobe   = FFPROBE_PATH

BASE = os.path.dirname(os.path.abspath(__file__))
P_SCRIPTS = os.path.join(BASE, "scripts")
P_ASSETS  = os.path.join(BASE, "assets")
P_AUDIO   = os.path.join(BASE, "audio")
os.makedirs(P_AUDIO, exist_ok=True)

ARQ_ROTEIRO = os.path.join(P_SCRIPTS, "roteiro_clipchamp.txt")
ARQ_TRILHA  = os.path.join(P_ASSETS,  "trilha_fundo.mp3")
ARQ_VOZ     = os.path.join(P_AUDIO,   "episodio_01_narracao.mp3")
ARQ_MIX     = os.path.join(P_AUDIO,   "episodio_01_mixado.mp3")

# ---- leitura do roteiro
if not os.path.isfile(ARQ_ROTEIRO):
    print("❌ Roteiro não encontrado:", ARQ_ROTEIRO); sys.exit(1)
with open(ARQ_ROTEIRO, "r", encoding="utf-8") as f:
    TEXTO = f.read().strip()
if not TEXTO:
    print("❌ Roteiro está vazio."); sys.exit(1)

# ---- geração da narração
async def gerar_narracao():
    print("🎙️ Gerando narração (voz neural pt-BR)...")
    com = edge_tts.Communicate(text=TEXTO, voice=VOZ_NEURAL, rate="+0%", volume="+0%")
    await com.save(ARQ_VOZ)
    if not os.path.isfile(ARQ_VOZ) or os.path.getsize(ARQ_VOZ) == 0:
        print("❌ Falha ao gerar narração."); sys.exit(1)
    print(f"✅ Narração gerada: {ARQ_VOZ}")

# ---- mix com trilha (com volume e fades)
def mixar_trilha():
    if not os.path.isfile(ARQ_TRILHA) or os.path.getsize(ARQ_TRILHA) == 0:
        print("❌ Trilha ausente/vazia em:", ARQ_TRILHA); sys.exit(1)

    print("🎵 Mixando trilha de fundo...")
    voz    = AudioSegment.from_file(ARQ_VOZ,    format="mp3")
    trilha = AudioSegment.from_file(ARQ_TRILHA, format="mp3")

    # aplica volume e fades na trilha
    trilha = trilha + TRILHA_VOLUME_DB
    if FADE_IN_MS  > 0: trilha = trilha.fade_in(FADE_IN_MS)
    if FADE_OUT_MS > 0: trilha = trilha.fade_out(FADE_OUT_MS)

    # repete a trilha até cobrir toda a voz
    while len(trilha) < len(voz):
        trilha += trilha
    trilha = trilha[:len(voz)]

    mix = voz.overlay(trilha)
    mix.export(ARQ_MIX, format="mp3")
    print(f"✅ Mix final salvo em: {ARQ_MIX}")

if __name__ == "__main__":
    asyncio.run(gerar_narracao())
    mixar_trilha()
    print("\n🚀 Podcast finalizado com sucesso!")
