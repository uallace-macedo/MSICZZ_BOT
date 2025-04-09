from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN

def main():
  application = ApplicationBuilder().token(BOT_TOKEN).build()
  print('Starting bot...')

  print('Polling...')
  application.run_polling()


if __name__ == '__main__':
  main()
