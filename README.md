# 🎧 Podcast — Eficiência em Movimento

🎥 **Ouça ou assista agora:**  
👉 [▶️ Abrir o player no GitHub Pages](https://gabrielsvdata.github.io/Projeto-eficiencia-em-movimento/)

> Se o player não carregar de imediato, aguarde a atualização do GitHub Pages (pode levar alguns minutos após o push).

---

## 📘 Sobre o projeto

O **Podcast “Eficiência em Movimento”** foi criado para apresentar, de forma acessível e envolvente, os conceitos centrais da **logística moderna**, com foco na **eficiência de armazenagem de equipamentos eletrônicos**.

O objetivo é **educar, inspirar e profissionalizar equipes de logística**, promovendo o entendimento de como práticas bem estruturadas impactam produtividade, sustentabilidade e tecnologia no setor.

---

## 🧠 Tecnologias utilizadas

| Etapa | Ferramenta / Biblioteca | Função |
|-------|--------------------------|--------|
| ✍️ Criação de roteiro | **ChatGPT (GPT-5)** | Criação de título e roteiro técnico do episódio. |
| 🖼️ Capa do podcast | **ChatGPT Image Generator (DALL-E)** | Geração automática de imagem de capa 1:1. |
| 🔊 Áudio narrado | **edge-tts / Coqui-TTS** | Síntese de voz humana natural em português. |
| 🎵 Mixagem | **PyDub + FFmpeg** | Combinação da voz narrada com trilha de fundo. |
| 🎬 Edição de vídeo | **MoviePy 2.2.1** | Criação do vídeo final (capa + áudio sincronizado). |
| 🌍 Publicação | **GitHub Pages** | Hospedagem gratuita do player de vídeo interativo. |

---

## ⚙️ Estrutura do projeto

```
/
├── assets/
│   └── capa_podcast.png
│
├── audio/
│   ├── episodio_01_narracao.mp3
│   ├── trilha_fundo.mp3
│   └── episodio_01_mixado.mp3
│
├── video/
│   └── episodio_01.mp4
│
├── docs/
│   └── index.html        # Página publicada no GitHub Pages
│
├── gerar_audio_musical.py
├── gerar_video.py
└── requirements.txt
```

---

## 🚀 Como funciona

1. O roteiro é escrito automaticamente via ChatGPT.  
2. O áudio é gerado com voz sintética e trilha sonora.  
3. O vídeo MP4 é criado com MoviePy (capa + áudio sincronizado).  
4. O GitHub Pages exibe o player direto no navegador.

---

## 💻 Execução local (opcional)

Para gerar o vídeo localmente:

```bash
pip install moviepy pydub ffmpeg-python
python gerar_video.py
```

O arquivo final será salvo em:
```
video/episodio_01.mp4
```

---

## 🔗 Links principais

🎧 **Player online:**  
[https://gabrielsvdata.github.io/Projeto-eficiencia-em-movimento/](https://gabrielsvdata.github.io/Projeto-eficiencia-em-movimento/)

📂 **Repositório GitHub:**  
[https://github.com/gabrielsvdata/Projeto-eficiencia-em-movimento](https://github.com/gabrielsvdata/Projeto-eficiencia-em-movimento)

---

## 🧾 Licença

Este projeto é **educacional** e demonstra o uso de **IA generativa** na criação e automação de conteúdo multimídia.  
Desenvolvido por **Gabriel Silvano Vieira**, 2025.

---

> “Eficiência é quando a tecnologia trabalha a favor das pessoas — e não o contrário.”
