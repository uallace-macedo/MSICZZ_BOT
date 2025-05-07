# 🤖 Telegram Music Bot 🎵

Um bot criado com Python que permite baixar músicas e playlists diretamente do YouTube via comandos no Telegram.

---

## 🚀 Funcionalidades

- `/start` — Inicia a conversa com o BOT
- `/help` — Mostra os comandos disponíveis
- `/dwm <url>` — Baixa uma música do YouTube (duração <= 10m10s>)
- `/dwm <url>, <url>, ...` — Baixa várias músicas do YouTube (duração <= 10m10s>)
- `/dwp <url>` — Baixa uma playlist do YouTube (apenas músicas com duração <= 10m10s>)

---

## 🛠️ Tecnologias usadas

- **Python 3.10+**
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [pytubefix](https://github.com/nficano/pytube)
- [pytest](https://github.com/pytest-dev/pytest)

---

## 🔒 Notas

- Para visualizar a tomada de decisões, desafios e etc., pode checar o `DIARIO.md`. Meu diário de bordo, onde anoto tudo que fiz, os desafios e soluções que encontrei durante o desenvolvimento.

- O comando de `help` é atualizado automaticamente conforme são adicionados mais diretórios de comandos com comandos. Bastando pré-configurar o `__init__.py` do diretório em questão definindo a categoria.
  ```js
  // Código Boilerplate
  from pathlib import Path
  from utils.commands import get_commands

  path = Path(__file__).parent

  // mude apenas o valor de 'category', conforme a categoria dos comandos em questão
  module_data = { 'category': '📦 Básico' }
  handlers = get_commands(path, __name__)

  module_data['commands'] = handlers
  ```
  Exemplo de uso: `src/commands/simple/__init__.py`

- É necessário em cada comando haver um atributo "`handler`", que deve ser gerado com a função `register_command()`.
  ```js
  from telegram import Update
  from telegram.ext import ContextTypes
  from utils.register import register_command

  async def start_command(update: Update, _: ContextTypes.DEFAULT_TYPE):
    ...

  handler = register_command(
    func=start_command,
    id='start',
    desc='Comando de inicio',
    long_desc='Descrição detalhada do comando, a ser mostrada com o /help nome_do_comando'
  )
  ```

---

## ☕ Considerações finais...
Este projeto nasceu da ideia de facilitar o download de músicas via Telegram de forma simples, e funcional.
Ainda está em desenvolvimento, mas já cumpre bem o papel principal — e novas funcionalidades estão a caminho.

Fique à vontade para usar, adaptar ou contribuir. E claro... aproveita o som 🎧
