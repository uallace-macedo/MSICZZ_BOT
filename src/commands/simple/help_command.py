from telegram import Update
from telegram.ext import ContextTypes
from utils.register import register_command

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text(
    '[🛠️] Comandos simples\n- /start: Comando de início\n - /help: Mostra os comandos disponíveis\n\n' +
    '[🎧] Comandos de música\n[em breve...]'
  )

handler = register_command(
  func=help_command,
  id='help',
  desc='Mostra os comandos disponíveis'
)
