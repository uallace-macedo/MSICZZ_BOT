from telegram import Update
from telegram.ext import ContextTypes

from utils.register import register_command
from utils.folders import delete_users_folder
from utils.download import download_music
from utils.text_format import get_final_url


async def download_music_command(update: Update, _: ContextTypes.DEFAULT_TYPE):
  sent_url: str = update.message.text
  final_url = get_final_url(sent_url)

  if 'error' in final_url:
    await update.message.reply_text(final_url['error'])

  status_message = await update.message.reply_text('[⏳] Iniciando o download...')
  download = download_music(final_url, update)

  if 'error' in download:
    await status_message.edit_text(download['error'])
    return

  await send_music(update, status_message, download)


async def send_music(update, status_message, download):
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
