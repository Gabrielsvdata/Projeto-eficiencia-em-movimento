# gerar_audio_edgetts.py
# ===========================================================
# Gera o áudio do podcast com voz neural da Microsoft Edge-TTS
# ===========================================================

import edge_tts
import asyncio
import os

# Caminhos
base_dir = os.path.dirname(os.path.abspath(__file__))
roteiro_path = os.path.join(base_dir, "scripts", "roteiro_clipchamp.txt")
output_dir = os.path.join(base_dir, "audio")
os.makedirs(output_dir, exist_ok=True)

# Lê o roteiro
with open(roteiro_path, "r", encoding="utf-8") as f:
    texto = f.read()

# Caminho do áudio de saída
output_file = os.path.join(output_dir, "episodio_01_narracao.mp3")

# Função principal
async def gerar_audio():
    print("🎙️ Gerando narração com voz neural (pt-BR)...")
    comunicador = edge_tts.Communicate(
        text=texto,
        voice="pt-BR-FranciscaNeural",  # voz feminina natural
        rate="+0%",  # velocidade
        volume="+0%"  # volume
    )
    await comunicador.save(output_file)
    print(f"✅ Narração gerada: {output_file}")

if __name__ == "__main__":
    asyncio.run(gerar_audio())
