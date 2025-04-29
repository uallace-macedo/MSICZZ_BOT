import os
import shutil


def get_downloads_folder() -> str:
  download_path = os.path.join(os.curdir, 'downloads')

  if not os.path.exists(download_path):
    os.mkdir(download_path)

  return download_path


def create_users_folder(id) -> str:
  download_path = get_downloads_folder()
  users_folder_path = os.path.join(download_path, str(id))

  if not os.path.exists(users_folder_path):
    os.mkdir(users_folder_path)

  return users_folder_path


def delete_users_folder(id):
  download_path = get_downloads_folder()
  users_folder_path = os.path.join(download_path, str(id))

  if os.path.exists(users_folder_path):
    shutil.rmtree(users_folder_path)
