from telegram.ext import BaseHandler, CommandHandler
from typing import Callable, Union, Dict

def register_command(
  func: Callable,
  id: Union[str, list[str]],
  desc: str
) -> Dict[str, Union[list[str], BaseHandler, str]]:

  if not isinstance(id, (list, str)):
    raise ValueError('Parâmetro <id> precisa ser uma string/lista de strings.')

  cmds = [id] if isinstance(id, str) else id
  handler = CommandHandler(cmds, func)

  return {
    'id': cmds,
    'description': desc,
    'cmd_handler': handler
  }
