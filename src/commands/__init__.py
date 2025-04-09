from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module

handlers =  []
handlers_raw = []
commands_by_category = {}
path = Path(__file__).parent

for _, name, _ in iter_modules([str(path)]):
  module = import_module(f'{__name__}.{name}')

  if hasattr(module, 'data'):
    data = getattr(module, 'data')

    if isinstance(data.get('handlers'), list):
      handlers.extend(data.get('handlers'))

    if isinstance(data.get('raw'), list):
      handlers_raw.extend(data['raw'])

for handler in handlers_raw:
  if not handler.get('active'):
    continue

  cmd_obj = handler['cmd']
  commands = cmd_obj.commands

  description = handler.get('description', '')
  category = handler.get('category')
  emoji = handler.get('emoji')
  key = f'{emoji} {category}'

  if key not in commands_by_category:
    commands_by_category[key] = []

  for cmd in commands:
    commands_by_category[key].append({f'/{cmd}': description})
