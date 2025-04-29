from pathlib import Path
from utils.commands import get_commands

path = Path(__file__).parent

module_data = { 'category': '🎸 Música' }
handlers = get_commands(path, __name__)

module_data['commands'] = handlers
