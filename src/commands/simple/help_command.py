from telegram import Update
from telegram.ext import ContextTypes
from utils.register import register_command
from .. import commands as cmds

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  message = ''
  for commands in cmds:
    message += f'*{commands['category']}*:\n'

    for command in commands['commands']:
      if len(command['id']) == 1:
        message += f'/{command['id'][0]}: {command['description']}\n'
      else:
        aliases = ', '.join([f'/{command}' for command in command['id']])
        message += f'/{command['id'][0] [{aliases}]}: {command['description']}\n'

    message += '\n'

  await update.message.reply_text(message, parse_mode='MarkdownV2')

handler = register_command(
  func=help_command,
  id='help',
  desc='Mostra os comandos disponíveis'
)
