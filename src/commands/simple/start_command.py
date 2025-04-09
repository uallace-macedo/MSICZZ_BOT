from telegram import Update
from telegram.ext import ContextTypes
from utils.register import register_command

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text('Olá, seja bem-vindo(a). Digite /help, para descobrir os comandos!')


handler = register_command(
  commands='start',
  callback=start_command,
  description='Inicia o BOT'
)
