from telegram import Update
from telegram.ext import ContextTypes
from utils.register import register_command

async def download_music(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text('Baixar música')


handler = register_command(
  commands='dm',
  callback=download_music,
  description='Baixe uma música, fornecendo a url. Uso: /dm <url do video>',
  category='Música',
  emoji='🎵'
)
