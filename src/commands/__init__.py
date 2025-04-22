from pkgutil import iter_modules
from importlib import import_module
from pathlib import Path

path = Path(__file__).parent
commands = []
handlers = []

for _, name, _ in iter_modules([str(path)]):
  module = import_module(f'{__name__}.{name}')

  if hasattr(module, 'module_data'):
    module_data = getattr(module, 'module_data')

    commands.append(module_data)
    cmds = [item['cmd_handler'] for item in module_data['commands']]
    handlers.extend(cmds)
