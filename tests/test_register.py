import pytest
from src.utils.register import register_command

def dummy(update, context):
  pass

def test_register_command_return():
  result = register_command(dummy, ['cmd'], 'Command description')

  assert result['cmd_handler'] != ''
  assert result['id'] != ''
  assert result['description'] != ''

  print(f'RETURN RESULT: {result}')

def test_register_command_id_value_error():
  pytest.raises(ValueError, match='<id> parameter must be a string or list[str]')
