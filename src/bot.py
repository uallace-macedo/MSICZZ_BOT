from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from commands import handlers

def main():
  application = ApplicationBuilder().token(BOT_TOKEN).build()
  print('Starting bot...')

  for handler in handlers:
    application.add_handler(handler)

  print('Polling...')
  application.run_polling()


if __name__ == '__main__':
  main()
