from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from commands import handlers

def main():
  print('[🤖] Starting...')
  application = ApplicationBuilder().token(BOT_TOKEN).build()

  for handler in handlers:
    print(handler)
    application.add_handler(handler)

  print('[🤖] Polling...')
  application.run_polling()


if __name__ == '__main__':
  main()
