import os
from typing import Final
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN: Final = os.environ.get('BOT_TOKEN')
BOT_USERNAME: Final = os.environ.get('BOT_USERNAME')
