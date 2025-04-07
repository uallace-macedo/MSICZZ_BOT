from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from utils.text_messages import HELP_TEXT

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_markdown_v2(HELP_TEXT)

handler = CommandHandler("help", help_command)
