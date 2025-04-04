from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text('Custom command')

handler = CommandHandler('custom', custom_command)
