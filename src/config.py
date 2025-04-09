import os
from dotenv import load_dotenv
from typing import Final

load_dotenv()
BOT_TOKEN: Final = os.environ.get('BOT_TOKEN')
BOT_USERNAME: Final = os.environ.get('BOT_USERNAME')
