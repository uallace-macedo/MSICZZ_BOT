from telegram import Update
from telegram.ext import ContextTypes

from pytubefix import Playlist

from utils.download import download_music
from utils.register import register_command
from utils.text_format import get_final_url


async def download_playlist_command(update: Update, _: ContextTypes.DEFAULT_TYPE):
  musics: list = []
  errors: list = []

  user_id = update.effective_user.id
  sent_url: str = update.message.text
  final_url = get_final_url(sent_url)

  if 'error' in final_url:
    await update.message.reply_text(final_url['error'])

  status_message = await update.message.reply_text('[⏳] Iniciando o download...')
  pl = Playlist(final_url)
  for music in pl.videos:
    download = download_music(music, update)

    if 'error' in download:
      errors.append({ 'title': download['title'], 'error': download['error'] })
    else:
      musics.append(download['title'])

  report = {'musics': musics, 'errors': errors}

  await send_report(status_message, report)
  # await send_musics(update, user_id)


async def send_report(status_message, report):
  musics = report['musics']
  errors = report['errors']

  errors.append({'title': 'abc', 'error': 'Erro msg'})
  errors.append({'title': 'abc2', 'error': 'Erro msg2'})
  errors.append({'title': 'abc3', 'error': 'Erro msg3'})

  message = f"""
[🎉] Download finalizado!
→ Downloads: {len(musics)} | Erros: {len(errors)}

[🎸] Músicas baixadas:
"""

  for index, music in enumerate(musics):
    message += f'{index + 1} - {music}\n'

  if len(errors) > 0:
    message += f'\n[❌] Erros:'

    for index, music in enumerate(errors):
      message += f'{index + 1} - {music['title']}\n'

  await status_message.edit_text(message)


async def send_musics(update, user_id):
  ...


handler = register_command(
  func=download_playlist_command,
  id=['dwp'],
  desc='Faça o download de uma playlist pública, acrescido de &lt;URL&gt;'
)
