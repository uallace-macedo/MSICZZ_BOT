from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from utils.text_messages import START_TEXT

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_markdown_v2(START_TEXT)

handler = CommandHandler("start", start_command)
