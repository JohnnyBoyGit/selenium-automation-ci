# tests/unit/test_infusion_logic.py
from src.logic.infusion_therapy_logic import InfusionTherapyLogic

def test_infusion_constants():
    assert InfusionTherapyLogic.EXPECTED_TITLE_PART == "INFUSION THERAPY"
    assert InfusionTherapyLogic.EXPECTED_PATH == "/infusion-therapy-2"
