import config
from commands import start_command, help_command, custom_command
from handlers import message_handler, error_handler
from telegram.ext import Application

if __name__ == '__main__':
  print('Starting boot...')
  app = Application.builder().token(config.TOKEN).build()

  app.add_handler(start_command.handler)
  app.add_handler(help_command.handler)
  app.add_handler(custom_command.handler)

  app.add_handler(message_handler.message_handler)
  app.add_error_handler(error_handler.error_handler)

  print('Polling...')
  app.run_polling(poll_interval=3)
