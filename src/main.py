from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN

def main():
  print('[🤖] Starting...')
  application = ApplicationBuilder().token(BOT_TOKEN).build()

  print('[🤖] Polling...')
  application.run_polling()


if __name__ == '__main__':
  main()
