import os
from pathlib import Path
from dotenv import load_dotenv

class GetKeyInfo:

    def get_key():
        dotenv_path=Path('Get_info/key.env')
        load_dotenv(dotenv_path=dotenv_path)
        return os.getenv('key')