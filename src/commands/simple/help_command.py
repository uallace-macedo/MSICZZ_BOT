from telegram import Update
from telegram.ext import ContextTypes
from utils.register import register_command
from utils.texts import generate_help_text
from commands import commands_by_category

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  msg = generate_help_text(commands_by_category)
  await update.message.reply_text(msg, parse_mode='MarkdownV2')


handler = register_command(
  commands='help',
  callback=help_command,
  description='Mostra os comandos disponíveis'
)
