import re
from unidecode import unidecode


def get_final_url(message: str) -> str:
  url_pattern: str = re.compile(r'<*https:\/\/(www\.)?(youtu\.be|youtube\.com)\/[^>]+>*')
  sent_url: str = message

  url = re.search(url_pattern, sent_url)
  if not url:
    return None

  final_url = re.sub(r'[<>]', '', url.group(0))
  return final_url


def clear_title(title) -> str:
  cleared_title: str = unidecode(title)
  cleared_title: str = re.sub(r'[^a-zA-Z0-9\s]', '', cleared_title)
  cleared_title: str = re.sub(r'\s+', '_', cleared_title)
  cleared_title: str = cleared_title.lower()

  return cleared_title
