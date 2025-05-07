from telegram.ext import BaseHandler, CommandHandler
from typing import Callable, Union, Dict

def register_command(
  func: Callable,
  id: Union[str, list[str]],
  desc: str,
  long_desc: str
) -> Dict[str, Union[list[str], BaseHandler, str]]:

  if not isinstance(id, (list, str)):
    raise ValueError('<id> parameter must be a string or list[str]')

  cmds = [id] if isinstance(id, str) else id
  handler = CommandHandler(cmds, func)

  return {
    'id': cmds,
    'description': desc,
    'cmd_handler': handler,
    'long_desc': long_desc
  }
