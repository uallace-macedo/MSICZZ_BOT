from telegram import Update
from telegram.ext import ContextTypes

from utils.register import register_command
from utils.folders import delete_users_folder
from utils.download import download_music, send_musics
from utils.text_format import get_final_url


async def download_music_command(update: Update, _: ContextTypes.DEFAULT_TYPE):
  sent_url: str = update.message.text
  to_download = get_final_url(sent_url)

  if 'error' in to_download:
    await update.message.reply_text(to_download['error'])
    return

  status_message = await update.message.reply_text('[⏳] Iniciando o download...')
  for link in to_download:
    download = download_music(link, update)

  if len(to_download) == 1 and 'error' in download:
    await status_message.edit_text(download['error'])
    return


  if len(to_download) == 1:
    await send_music(update, status_message, download)
    return

  await status_message.edit_text('[🎉] Download finalizado!')
  await send_musics(update, update.effective_user.id, 'Músicas')


async def send_music(update, status_message, download):
  song_path = download['song_path']
  title = download['title']

  await status_message.edit_text('[🎉] Download finalizado!')
  await update.message.reply_audio(audio=open(song_path, 'rb'), title=title)
  delete_users_folder(update.effective_user.id)


handler = register_command(
  func=download_music_command,
  id='dwm',
  desc='Faça o download de uma música, acrescido de &lt;URL&gt;',
  long_desc='Faça o download da(s) música(s):\n\nExemplo: /dwm www.youtube.com/watch?v=UtF6Jej8yb4&ab_channel=AviciiOfficialVEVO' +
  '\n\nVocê pode baixar várias músicas colocando uma vírgula entre os links.\n\nExemplo: /dwm www.youtube.com/watch?v=UtF6Jej8yb4&ab_channel=AviciiOfficialVEVO, https://www.youtube.com/watch?v=TRjLYpXeofA&ab_channel=MarianneBeaulieu-Topic\n\nObs: Só serão baixadas músicas com no máximo 10min10s de duração'
)
