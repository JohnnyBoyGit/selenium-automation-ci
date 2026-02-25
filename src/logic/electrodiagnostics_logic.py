# src/logic/electrodiagnostics_logic.py
from src.logic.common_logic import CommonLogic

class ElectroDiagnosticsLogic:
    # SIT expectations
    EXPECTED_TITLE_PART = "ELECTRODIAGNOSTIC"
    EXPECTED_PATH = "/electrodiagnostic"
    
    # We just link to the common logic here
    is_valid_phone_format = CommonLogic.is_valid_phone_format
    is_valid_address = CommonLogic.is_valid_address

