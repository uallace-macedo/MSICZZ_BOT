import os
from zipfile import ZipFile, ZIP_DEFLATED
import shutil


def get_downloads_folder() -> str:
  download_path = os.path.join(os.curdir, 'downloads')

  if not os.path.exists(download_path):
    os.mkdir(download_path)

  return download_path


def get_users_folder(id) -> str:
  download_path = get_downloads_folder()
  users_folder_path = os.path.join(download_path, str(id))

  return users_folder_path


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


def zip_file(directory, zip_name):
  with ZipFile(zip_name, 'w', compression=ZIP_DEFLATED) as zf:
    for dirpath, _, filenames in os.walk(directory):
      for filename in filenames:
        full_path: str = os.path.join(dirpath, filename)
        relative_path: str = os.path.relpath(full_path, directory)

        zf.write(full_path, relative_path)

  return zip_name
