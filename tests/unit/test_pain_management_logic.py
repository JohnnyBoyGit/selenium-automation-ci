# tests/unit/test_pain_management_logic.py
from src.logic.pain_management_logic import PainManagementLogic

def test_pain_mgmt_constants():
    assert PainManagementLogic.EXPECTED_TITLE_PART == "PAIN MANAGEMENT"
    assert PainManagementLogic.EXPECTED_PATH == "/pain-management"
