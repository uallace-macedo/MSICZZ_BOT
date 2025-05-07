import re


def get_final_url(sent_url: str) -> str:
  urls: list[str] = []
  url_pattern: str = re.compile(r"[<]?(https:\/\/)?(www\.)?(youtu\.be|youtube\.com)\/([^\s<>'\,]+)[>]*")

  result = re.finditer(url_pattern, sent_url)

  if not any(sent_url):
    return {'error': '[❌] Por favor, forneça uma URL válida!'}

  for r in result:
      final_url = re.sub(r'[<>,]', '', r.group(0))
      if not final_url.startswith('https://'):
        final_url = f'https://{final_url}'

      urls.append(final_url)

  return urls
