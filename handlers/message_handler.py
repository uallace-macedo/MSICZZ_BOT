from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
import config

def handle_response(text: str) -> str:
  processed: str = text.lower()

  if 'hello' in processed:
    return 'Heyy'

  if 'how are you' in processed:
    return 'I am gr8!'

  return 'I donnot understand what u wrote...'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
  message_type: str = update.message.chat.type
  text: str = update.message.text

  print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

  if message_type == 'group':
    if config.BOT_USERNAME in text:
      new_text: str = text.replace(config.BOT_USERNAME, '').strip()
      response: str = handle_response(new_text)
    else:
      return
  else:
    response: str = handle_response(text)

  print('Bot: ', response)
  await update.message.reply_text(response)

message_handler = MessageHandler(filters.TEXT, handle_message)
