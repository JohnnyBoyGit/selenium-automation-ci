# src/logic/ime_logic.py
from src.logic.common_logic import CommonLogic

class ImeLogic:
    # UNIQUE TO THIS PAGE
    EXPECTED_TITLE_PART = "INDEPENDENT MEDICAL EXAMS"
    EXPECTED_PATH = "/independent-medical-exams-2"
    
    # REUSABLE FROM COMMON LOGIC
    is_valid_phone_format = CommonLogic.is_valid_phone_format
    is_valid_address = CommonLogic.is_valid_address
