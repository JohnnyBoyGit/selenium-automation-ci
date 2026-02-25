# src/logic/home_logic.py
from src.logic.common_logic import CommonLogic

class HomeLogic:
    # UNIQUE TO HOME
    EXPECTED_PATH = "" # Base URL
    EXPECTED_RATING_TEXT = "EXCELLENT"
    
    # URL Mapping for the various buttons on the home page
    URL_MAP = {
        "BUTTON_READ_ME": "about",
        "BUTTON_VIEW_ALL_SERVICES": "services",
        "BUTTON_BOOK_AN_APPOINTMENT_1": "booking",
        "BUTTON_BOOK_AN_APPOINTMENT_2": "booking",
        "BUTTON_BOOK_AN_APPOINTMENT_3": "booking",
        "BUTTON_BOOK_AN_APPOINTMENT_4": "booking",
        "BUTTON_SCHEDULE_NOW": "booking"
    }

    # REUSABLE FROM COMMON LOGIC
    is_valid_phone_format = CommonLogic.is_valid_phone_format
    is_valid_address = CommonLogic.is_valid_address

    @staticmethod
    def get_url_expectation(key):
        return HomeLogic.URL_MAP.get(key, "")

    @staticmethod
    def is_rating_valid(text):
        return HomeLogic.EXPECTED_RATING_TEXT in text.upper()
