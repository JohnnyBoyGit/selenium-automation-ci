# src/logic/infusion_therapy_logic.py
from src.logic.common_logic import CommonLogic

class InfusionTherapyLogic:
    # UNIQUE TO THIS PAGE
    EXPECTED_TITLE_PART = "INFUSION THERAPY"
    EXPECTED_PATH = "/infusion-therapy-2"
    
    # REUSABLE FROM COMMON LOGIC
    is_valid_phone_format = CommonLogic.is_valid_phone_format
    is_valid_address = CommonLogic.is_valid_address
