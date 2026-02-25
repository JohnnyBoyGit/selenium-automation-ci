# src/logic/prp_logic.py
from src.logic.common_logic import CommonLogic

class PrpLogic:
    # UNIQUE TO THIS PAGE
    EXPECTED_TITLE_PART = "PLATELET RICH PLASMA"
    EXPECTED_PATH = "platelet-rich-plasma-prp"
    
    # REUSABLE FROM COMMON LOGIC
    is_valid_phone_format = CommonLogic.is_valid_phone_format
    is_valid_address = CommonLogic.is_valid_address
