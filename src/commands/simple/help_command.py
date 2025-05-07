from telegram import Update
from telegram.ext import ContextTypes
from utils.register import register_command
from utils.commands import get_command_details
from .. import commands as cmds

async def help_command(update: Update, _: ContextTypes.DEFAULT_TYPE):
  msg: str = update.message.text.split()
  if len(msg) > 1:
    msg: str = get_command_details(msg[1])
    await update.message.reply_text(msg, disable_web_page_preview=True)
    return

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

  message += 'Digite <b>/help nome_do_comando</b> para ver uma descrição detalhada do comando'

  await update.message.reply_text(message, parse_mode='HTML')

handler = register_command(
  func=help_command,
  id='help',
  desc='Mostra os comandos disponíveis',
  long_desc='Comando que lista todos os comandos.\n\nDigite /help nome_do_comando para ver uma descrição detalhada do comando'
)
