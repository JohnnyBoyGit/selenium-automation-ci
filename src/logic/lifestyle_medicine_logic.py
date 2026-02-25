# src/logic/lifestyle_logic.py
from src.logic.common_logic import CommonLogic

class LifestyleMedicineLogic:
    # URL Mapping for various links on this page
    URL_MAP = {
        "IV_THERAPY": "infusion-therapy",
        "HAIR_RESTORATION": "platelet-rich-plasma-prp",
        "REVITALIZE": "infusion-therapy" # Adjust if different
    }

    EXPECTED_PATH = "/lifestyle-medicine-2"
    EXPECTED_TITLE = "LIFESTYLE MEDICINE"

    # Reusable common logic
    is_valid_phone_format = CommonLogic.is_valid_phone_format
    is_valid_address = CommonLogic.is_valid_address

    @staticmethod
    def get_url_expectation(key):
        return LifestyleMedicineLogic.URL_MAP.get(key, "")
