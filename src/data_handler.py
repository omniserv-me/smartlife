import os
from dotenv import load_dotenv, find_dotenv, set_key, get_key

prod = os.environ.get("PROD") in {"true", "True", "TRUE"}
# read and write both to the .env and environ for local debug purposes
# tbh I was just too lazy to remove .env support
class DataHandler:
    def __init__(self):
        if not prod:
            self.dotenv_file = find_dotenv()
            load_dotenv(self.dotenv_file)

    def write(self, key: str, value: str):
        key=key.upper()
        if not prod:
            load_dotenv(self.dotenv_file)
            set_key(self.dotenv_file, key, value)
        os.environ[f"{key}"] = f"{value}"

    def get(self, key: str) -> str | None:
        key = key.upper()
        result = self.get_fromOS(key)
        if result is not None:
            return result
        if not prod:
            load_dotenv(self.dotenv_file)
            return get_key(self.dotenv_file, key)
        return None

    def get_fromOS(self, key: str) -> str | None:
        return os.environ.get(f"{key}")