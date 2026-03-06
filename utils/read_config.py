import configparser
from pathlib import Path

# Path relative to this file: ../../Configurations/config.ini
# .parent (utils) -> .parent (Project Root)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = PROJECT_ROOT / "Configurations" / "config.ini"

config = configparser.RawConfigParser()

# This will print the EXACT path in the GitHub log if it fails
if not CONFIG_PATH.exists():
    raise FileNotFoundError(f"CRITICAL: Config not found at {CONFIG_PATH}")

config.read(str(CONFIG_PATH))

class ReadConfig:
    @staticmethod
    def get_application_url():
        return config.get('common info', 'baseURL')

    @staticmethod
    def get_useremail():
        return config.get('common info', 'useremail')
