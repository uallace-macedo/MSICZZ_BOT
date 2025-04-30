import os
from telegram import Update
from pytubefix import YouTube
from pytubefix.exceptions import VideoUnavailable, VideoPrivate, MembersOnly, AgeRestrictedError, RegexMatchError, PytubeFixError

from utils.folders import create_users_folder
from utils.text_format import clear_title

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
