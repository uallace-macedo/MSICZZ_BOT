from commands import commands as commands_group
from telegram.ext import BaseHandler
from typing import Dict, Union

from pathlib import Path
from pkgutil import iter_modules
from importlib import import_module

def get_commands(
  path: Path,
  package_name: str
) -> list[Dict[str, Union[list[str], BaseHandler, str]]]:
  """Função responsável por iterar e retornar o handler de todos os comandos de um módulo.

  Args:
    path (Path): Nome do pacote pai (e.g., 'commands.simple' / 'commands.music').
    package_name (str): Caminho para o diretório do módulo.

  Returns:
    list (Dict[str, Union[list[str], BaseHandler, str]]): Lista dos handlers presentes em cada módulo.

  """
  handlers = []

  for _, name, _ in iter_modules([str(path)]):
    module = import_module(f'{package_name}.{name}')

    if hasattr(module, 'handler'):
      result = getattr(module, 'handler')
      handlers.append(result)

  return handlers


def get_command_details(command: str) -> str:

  for category in commands_group:
    for cm in category['commands']:
      if(command in cm['id']):
        return f'Comando: {command}\n{cm['long_desc']}\n'

  return '[❌] Comando não encontrado!'
