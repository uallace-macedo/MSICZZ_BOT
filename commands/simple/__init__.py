from . import start_command, help_command, custom_command

handlers = [
  start_command.handler,
  help_command.handler,
  custom_command.handler
]
