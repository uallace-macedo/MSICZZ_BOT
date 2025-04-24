from telegram import Update
from telegram.ext import ContextTypes
from utils.register import register_command
from .. import commands as cmds

async def help_command(update: Update, _: ContextTypes.DEFAULT_TYPE):
  message = ''
  for commands in cmds:
    message += f'<b>{commands['category']}</b>:\n'

    for command in commands['commands']:
      if len(command['id']) == 1:
        message += f'/{command['id'][0]}: {command['description']}\n'
      else:
        cmdsAndAliases = ', '.join([f'/{command}' for command in command['id']])
        message += f"{cmdsAndAliases}: {command['description']}\n"

    message += '\n'

  await update.message.reply_text(message, parse_mode='HTML')

handler = register_command(
  func=help_command,
  id='help',
  desc='Mostra os comandos disponíveis'
)
