import os
from telegram import Update
from pytubefix import YouTube
from pytubefix.exceptions import VideoUnavailable, VideoPrivate, MembersOnly, AgeRestrictedError, RegexMatchError, PytubeFixError

from utils.folders import create_users_folder, get_users_folder, zip_file, delete_users_folder


def download_music(video_url: str, update: Update):
  yt: YouTube

  try:
    if isinstance(video_url, YouTube):
      yt = video_url
    else:
      yt = YouTube(video_url)

    if yt.length > (10 * 60) + 10:
      return {'error': '[🧮] Não foi possível fazer o download. Parece que este vídeo possui mais de 10min...'}

    user_id: int = update.effective_user.id
    users_folder = create_users_folder(user_id)

    title: str = yt.title

    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(users_folder, f'{title}.mp3')

    song_path: str = os.path.join(users_folder, title) + '.mp3'
    return {'song_path': song_path, 'title': title}

  except VideoUnavailable:
    return {'error': '[❌] Não foi possível fazer o download. Parece que este vídeo está indisponível...', 'title': title}
  except VideoPrivate:
    return {'error': '[🔒] Não foi possível fazer o download. Parece que este vídeo está privado...'}
  except MembersOnly:
    return {'error': '[👑] Não foi possível fazer o download. Parece que este vídeo é apenas para membros...', 'title': title}
  except AgeRestrictedError:
    return {'error': '[🔞] Não foi possível fazer o download. Parece que este vídeo tem restrição de idade...', 'title': title}
  except RegexMatchError:
    return {'error': '[⚠️] Não foi possível fazer o download. Parece que houve um erro ao processar o vídeo...', 'title': title}
  except PytubeFixError:
    return {'error': '[🐞] Não foi possível fazer o download. Parece que houve um erro ao baixar o vídeo...', 'title': title}
  except Exception as e:
    print(e)
    return {'error': '[🔥] Não foi possível fazer o download. Parece que houve um erro inesperado...'}


async def send_musics(update: Update, user_id: int, title: str):
  zip_name: str = os.path.join(os.curdir, 'downloads', 'zips', f'{str(user_id)}.zip')
  users_folder: str = get_users_folder(user_id)

  zip_path = zip_file(users_folder, zip_name)
  await update.message.reply_document(zip_path, filename=f'{title}.zip')

  os.remove(zip_path)
  delete_users_folder(user_id)
