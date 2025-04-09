from telegram.ext import BaseHandler
from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module

def load_handler(path: Path, module_name: str) -> list[BaseHandler]:
  """Carrega os comandos da pasta especifica"""
  handlers = []
  handlers_raw = []

  for _, name, _ in iter_modules([str(path)]):
    module = import_module(f'{module_name}.{name}')

    if hasattr(module, 'handler'):
      command_handler = getattr(module, 'handler')
      if command_handler.get('active', False) and isinstance(command_handler.get('cmd'), BaseHandler):
        handlers.append(command_handler['cmd'])
        handlers_raw.append(command_handler)

  return { 'handlers': handlers, 'raw': handlers_raw }
