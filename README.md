# 🎧 Podcast — Eficiência em Movimento

Assista online (GitHub Pages): **[▶️ Abrir o player](https://SEU_USUARIO.github.io/SEU_REPO/)**

> Se o link acima ainda não funcionar, aguarde a publicação do GitHub Pages (geralmente alguns minutos após o push) e recarregue.

## Como funciona
- `audio/episodio_01_mixado.mp3`: narração + trilha, pronto.
- `video/episodio_01.mp4`: gerado a partir da capa estática + áudio final.
- `docs/index.html`: página com o player `<video>` para o GitHub Pages.

## Rodar local (opcional)
Para quem quiser gerar o MP4 localmente:

```bash
pip install moviepy
python gerar_video.py
