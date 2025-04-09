import re

def escape_markdown(text: str) -> str:
  """
  Escapa caracteres especiais conforme a especificação do Telegram MarkdownV2.
  """
  escape_chars = r'\_*[]()~`>#+-=|{}.!'
  return re.sub(r'([{}])'.format(re.escape(escape_chars)), r'\\\1', text)
