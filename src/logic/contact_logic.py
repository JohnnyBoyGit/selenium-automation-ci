# src/logic/contact_logic.py
from src.logic.common_logic import CommonLogic

class ContactLogic:

    EXPECTED_PATH = "/contact"
    
    CORE_DATA = {
        "ZIP_CODE": "91436",
        "CITY": "Encino",
        "MAP_TITLE_PART": "Ventura Blvd"
    }

    # Reference the common logic
    is_valid_phone_format = CommonLogic.is_valid_phone_format
    is_valid_address = CommonLogic.is_valid_address

    @staticmethod
    def is_valid_email_format(email_text):
        """Email logic is unique to Contact/Footer, so we keep it here or move to common later."""
        return "@" in email_text and "." in email_text

    @staticmethod
    def get_data(key):
        return ContactLogic.CORE_DATA.get(key, "")
