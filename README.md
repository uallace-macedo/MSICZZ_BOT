# 🤖 Telegram Music Bot 🎵

Um bot criado com Python que permite baixar músicas e playlists diretamente do YouTube via comandos no Telegram.

---

## 🚀 Funcionalidades

- `/start` — Inicia a conversa com o BOT
- `/help` — Mostra os comandos disponíveis
- `/download_music <url>` — Baixa e envia o áudio de um vídeo do YouTube 🎧

---

## 🛠️ Tecnologias usadas

- **Python 3.10+**
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [pytubefix](https://github.com/nficano/pytube) (fork ativo do pytube)
- `uuid` para nomes únicos temporários
- `shutil`, `os`, `re` e outros nativos

---

## 🔒 Notas

- Os downloads são organizados por ID do usuário dentro da pasta downloads/, evitando conflitos entre usuários.

---

## 🧠 Possibilidades futuras
- Pré-visualização de vídeos com thumbnail, título e duração

- Conversão com ffmpeg para melhor qualidade e formatos

- Sistema de anti-flood e limitação de uso por usuário

---

## ☕ Considerações finais...
Este projeto nasceu da ideia de facilitar o download de músicas via Telegram de forma simples, direta e funcional.
Ainda está em desenvolvimento, mas já cumpre bem o papel principal — e novas funcionalidades estão a caminho.

Fique à vontade para usar, adaptar ou contribuir. E claro... aproveita o som 🎧
