import configparser
import os

# 1. Get the directory where THIS file (read_config.py) is located
# 2. Go up one level to get the Project Root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 3. Build the path to the config file (Works on both Windows and Linux)
CONFIG_PATH = os.path.join(PROJECT_ROOT, "Configurations", "config.ini")

config = configparser.RawConfigParser()

# Verify the file actually exists to provide a better error message if it fails
if not os.path.exists(CONFIG_PATH):
    raise FileNotFoundError(f"Config file not found at: {CONFIG_PATH}")

config.read(CONFIG_PATH)

class ReadConfig:
    @staticmethod
    def get_application_url():
        return config.get('common info', 'baseURL')

    @staticmethod
    def get_useremail():
        return config.get('common info', 'useremail')
