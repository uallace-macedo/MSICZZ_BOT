from pathlib import Path
from utils.load import load_handler

data = load_handler(Path(__file__).parent, __name__)
