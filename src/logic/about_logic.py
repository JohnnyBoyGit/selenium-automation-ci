# src/logic/about_logic.py
from src.logic.common_logic import CommonLogic

class AboutLogic:
    # 1. ADD THIS LINE (This fixes all 7 failures)
    EXPECTED_PATH = "/about" 

    # 2. Keep your existing snippets for internal links
    URL_SNIPPETS = {
        "APPOINTMENT_LINK": "booking"
    }

    # Reusable from Common Logic
    is_valid_phone_format = CommonLogic.is_valid_phone_format
    is_valid_address = CommonLogic.is_valid_address

    @staticmethod
    def get_url_expectation(key):
        return AboutLogic.URL_SNIPPETS.get(key, "")
