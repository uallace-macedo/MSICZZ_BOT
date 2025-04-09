from telegram.ext import CommandHandler
from typing import Union, List, Callable

def register_command(
  commands: Union[str, List[str]],
  callback: Callable,
  description: str,
  category: str = 'Geral',
  emoji: str = '📌',
  active: bool = True
) -> dict:
  """Registra um comando com descricao, emoji e categoria, informando ainda se esta ativo."""
  if isinstance(commands, str):
    commands = [commands]

  handler = CommandHandler(commands, callback)

  return {
    'active': active,
    'description': description,
    'category': category,
    'emoji': emoji,
    'cmd': handler
  }
