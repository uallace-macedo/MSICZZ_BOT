import os
import re
from uuid import uuid4
from pytubefix import YouTube
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from utils.file_utils import create_user_folder, delete_if_empty, clean_filename


async def download_music_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  if not context.args:
    await update.message.reply_text('❗ Envia uma URL do YouTube. Exemplo:\n/download_music <url>')
    return

  url: str = context.args[0]
  msg: str = await update.message.reply_text('🎧 Baixando a música, segura aí...')

  try:
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()

    user_id = update.effective_user.id
    user_folder = create_user_folder(user_id)

    raw_filename = f'{uuid4()}.mp3'
    clean_name = clean_filename(yt.title)
    final_filename = f'{clean_name}.mp3'

    raw_path = os.path.join(user_folder, raw_filename)
    final_path = os.path.join(user_folder, final_filename)

    stream.download(filename=raw_filename, output_path=user_folder)
    os.rename(raw_path, final_path)

    with open(final_path, 'rb') as audio:
      await update.message.reply_audio(
        audio,
        title=yt.title,
        performer=yt.author,
        filename=final_filename
      )

    os.remove(final_path)
    delete_if_empty(user_folder)
    await msg.edit_text('✅ Música baixada com sucesso!')
  except Exception as e:
    print('Erro ao baixar música:', e)
    await msg.edit_text('❌ Deu ruim ao tentar baixar a música. Tente novamente!')


handler = CommandHandler("download_music", download_music_command)
