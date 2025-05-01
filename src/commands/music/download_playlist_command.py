import os

from telegram import Update
from telegram.ext import ContextTypes

from pytubefix import Playlist

from utils.download import download_music
from utils.register import register_command
from utils.text_format import get_final_url
from utils.folders import zip_file, get_users_folder, delete_users_folder


async def download_playlist_command(update: Update, _: ContextTypes.DEFAULT_TYPE):
  musics: list = []
  errors: list = []

  user_id = update.effective_user.id
  sent_url: str = update.message.text
  final_url = get_final_url(sent_url)

  if 'error' in final_url:
    await update.message.reply_text(final_url['error'])
    return

  status_message = await update.message.reply_text('[⏳] Iniciando o download...')
  pl = Playlist(final_url)
  for music in pl.videos:
    download = download_music(music, update)

    if 'error' in download:
      errors.append({ 'title': download['title'], 'error': download['error'] })
    else:
      musics.append(download['title'])

  report = {'musics': musics, 'errors': errors}

  await send_report(status_message, report, pl.title)
  await send_musics(update, user_id, pl.title)


async def send_report(status_message, report, title):
  musics = report['musics']
  errors = report['errors']

  message = f"""
[🎉] Download finalizado!
→ Playlist: {title}
→ Downloads: {len(musics)} | Erros: {len(errors)}
"""

  await status_message.edit_text(message)


async def send_musics(update: Update, user_id: int, title: str):
  zip_name: str = os.path.join(os.curdir, 'downloads', 'zips', f'{str(user_id)}.zip')
  users_folder: str = get_users_folder(user_id)

  zip_path = zip_file(users_folder, zip_name)
  await update.message.reply_document(zip_path, filename=f'{title}.zip')

  os.remove(zip_path)
  delete_users_folder(user_id)


handler = register_command(
  func=download_playlist_command,
  id=['dwp'],
  desc='Faça o download de uma playlist pública, acrescido de &lt;URL&gt;'
)
