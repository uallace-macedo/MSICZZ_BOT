from telegram import Update
from telegram.ext import ContextTypes
from utils.register import register_command

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text('🎧 Opa!!! Digite /help para descobrir os comandos disponíveis!')


handler = register_command(
  func=start_command,
  id='start',
  desc='Comando de inicio'
)
