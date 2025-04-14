from .help_command import handler as help_handler
from .start_command import handler as start_handler

handlers = [
  help_handler['cmd_handler'],
  start_handler['cmd_handler']
]
