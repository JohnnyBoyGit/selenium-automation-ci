# src/logic/pain_management_logic.py
from src.logic.common_logic import CommonLogic

class PainManagementLogic:
    # UNIQUE TO THIS PAGE
    EXPECTED_TITLE_PART = "PAIN MANAGEMENT"
    EXPECTED_PATH = "/pain-management"
    
    # REUSABLE FROM COMMON LOGIC
    is_valid_phone_format = CommonLogic.is_valid_phone_format
    is_valid_address = CommonLogic.is_valid_address
