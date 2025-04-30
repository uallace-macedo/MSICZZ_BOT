import os
import re

from pytubefix import YouTube
from pytubefix.exceptions import VideoUnavailable, VideoPrivate, MembersOnly, AgeRestrictedError, RegexMatchError, PytubeFixError

from telegram import Update
from telegram.ext import ContextTypes

from utils.register import register_command
from utils.folders import create_users_folder, delete_users_folder
from utils.text_format import clear_title

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

  if download['error']:
    print(download['error'])
    return

  song_path = download['song_path']
  title = download['title']

  await status_message.edit_text('[🎉] Download finalizado!')
  await update.message.reply_audio(audio=open(song_path, 'rb'), title=title)
  delete_users_folder(update.effective_user.id)

def download_music(video_url: str, update: Update):
  user_id: int = update.effective_user.id
  users_folder = create_users_folder(user_id)

  try:
    yt = YouTube(video_url)
    title: str = yt.title

    cleared_title = clear_title(title)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(users_folder, f'{cleared_title}.mp3')

    song_path: str = os.path.join(users_folder, cleared_title) + '.mp3'
    return {'song_path': song_path, 'title': title}
  except VideoUnavailable:
    return {'error': '[❌] Não foi possível fazer o download. Parece que este vídeo está indisponível...'}
  except VideoPrivate:
    return {'error': '[🔒] Não foi possível fazer o download. Parece que este vídeo está privado...'}
  except MembersOnly:
    return {'error': '[👑] Não foi possível fazer o download. Parece que este vídeo é apenas para membros...'}
  except AgeRestrictedError:
    return {'error': '[🔞] Não foi possível fazer o download. Parece que este vídeo tem restrição de idade...'}
  except RegexMatchError:
    return {'error': '[⚠️] Não foi possível fazer o download. Parece que houve um erro ao processar o vídeo...'}
  except PytubeFixError:
    return {'error': '[🐞] Não foi possível fazer o download. Parece que houve um erro ao baixar o vídeo...'}
  except Exception as e:
    print(e)
    return {'error': '[🔥] Não foi possível fazer o download. Parece que houve um erro inesperado...'}


handler = register_command(
  func=download_music_command,
  id='dwm',
  desc='Faça o download de uma música, acrescido de &lt;URL&gt;'
)
