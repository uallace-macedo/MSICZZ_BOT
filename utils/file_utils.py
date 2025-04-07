import os
import re


def create_download_root():
  if not os.path.exists("downloads"):
    os.makedirs("downloads")


def create_user_folder(user_id: int) -> str:
  folder = os.path.join("downloads", str(user_id))
  os.makedirs(folder, exist_ok=True)
  return folder

def delete_if_empty(folder: str):
  if os.path.exists(folder) and not os.listdir(folder):
    os.rmdir(folder)


def clean_filename(name):
  return re.sub(r'[\\/*?:"<>|]', '', name)
