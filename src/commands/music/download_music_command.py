import re

from telegram import Update
from telegram.ext import ContextTypes

from utils.register import register_command
from utils.folders import delete_users_folder
from utils.download import download_music

async def download_music_command(update: Update, _: ContextTypes.DEFAULT_TYPE):
  url_pattern: str = re.compile(r'<*https:\/\/(www\.)?(youtu\.be|youtube\.com)\/[^>]+>*')
  sent_url: str = update.message.text

  url = re.search(url_pattern, sent_url)
  if not url:
    await update.message.reply_text('[❌] Por favor, forneça uma URL válida!')
    return

  final_url = re.sub(r'[<>]', '', url.group(0))
  status_message = await update.message.reply_text('[⏳] Iniciando o download...')
  download = download_music(final_url, update)

  if 'error' in download:
    await status_message.edit_text(download['error'])
    return

  song_path = download['song_path']
  title = download['title']

  await status_message.edit_text('[🎉] Download finalizado!')
  await update.message.reply_audio(audio=open(song_path, 'rb'), title=title)
  delete_users_folder(update.effective_user.id)

handler = register_command(
  func=download_music_command,
  id='dwm',
  desc='Faça o download de uma música, acrescido de &lt;URL&gt;'
)
