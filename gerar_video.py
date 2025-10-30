# gerar_video.py — Gera MP4 (capa estática + áudio final) - Compatível MoviePy 2.2.1
import os, sys
from moviepy import ImageClip, AudioFileClip, ColorClip, CompositeVideoClip

BASE       = os.path.dirname(os.path.abspath(__file__))
P_ASSETS   = os.path.join(BASE, "assets")
P_AUDIO    = os.path.join(BASE, "audio")
P_OUT      = os.path.join(BASE, "video")
os.makedirs(P_OUT, exist_ok=True)

CAPA_PATH  = os.path.join(P_ASSETS, "capa_podcast.png")   # imagem 1:1 ou 16:9
AUDIO_PATH = os.path.join(P_AUDIO,  "episodio_01_mixado.mp3")
VIDEO_OUT  = os.path.join(P_OUT,    "episodio_01.mp4")

# ---- checagens
if not os.path.isfile(CAPA_PATH):
    print(f"❌ Capa não encontrada: {CAPA_PATH}"); sys.exit(1)
if not os.path.isfile(AUDIO_PATH) or os.path.getsize(AUDIO_PATH) == 0:
    print(f"❌ Áudio final não encontrado/vazio: {AUDIO_PATH}"); sys.exit(1)

# ---- carrega mídia
print("🎬 Carregando mídia…")
audio = AudioFileClip(AUDIO_PATH)
img   = ImageClip(CAPA_PATH)

# define duração do vídeo pela duração do áudio (API 2.x)
img = img.with_duration(audio.duration)

# ajusta resolução (use .resized)
VIDEO_SIZE = (1920, 1080)
img = img.resized(height=VIDEO_SIZE[1])

# cria fundo preto e centraliza a capa
bg = ColorClip(size=VIDEO_SIZE, color=(0, 0, 0), duration=audio.duration)
img = img.with_position("center")

# combina imagem e som
final = CompositeVideoClip([bg, img]).with_audio(audio)

# exporta vídeo
print("📤 Exportando MP4… (pode demorar um pouco)")
final.write_videofile(
    VIDEO_OUT,
    codec="libx264",
    audio_codec="aac",
    fps=24,
    bitrate="4000k",
    audio_bitrate="192k"
)

print(f"✅ Vídeo gerado: {VIDEO_OUT}")
