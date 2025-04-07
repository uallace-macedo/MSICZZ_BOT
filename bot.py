import config
from commands import handlers as command_handlers
from handlers import  error_handler
from telegram.ext import Application
from utils.file_utils import create_download_root

if __name__ == '__main__':
  print('Starting bot...')
  create_download_root()
  app = Application.builder().token(config.TOKEN).build()

  for handler in command_handlers:
    app.add_handler(handler)

  app.add_error_handler(error_handler.error_handler)

  print('Polling...')
  app.run_polling(poll_interval=3)
