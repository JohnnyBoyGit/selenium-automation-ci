# tests/unit/test_lifestyle_medicine_logic.py
from src.logic.lifestyle_medicine_logic import LifestyleMedicineLogic

def test_lifestyle_url_logic():
    assert LifestyleMedicineLogic.get_url_expectation("IV_THERAPY") == "infusion-therapy"
    assert LifestyleMedicineLogic.get_url_expectation("HAIR_RESTORATION") == "platelet-rich-plasma-prp"

def test_lifestyle_constants():
    assert LifestyleMedicineLogic.EXPECTED_PATH == "/lifestyle-medicine-2"
