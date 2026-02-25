# tests/unit/test_services_logic.py
import pytest
from src.logic.services_logic import ServicesLogic

def test_image_slug_mapping():
    # Verify a few critical mappings
    assert ServicesLogic.get_slug("PAIN") == "pain-management"
    assert ServicesLogic.get_slug("ELECTRO") == "electrodiagnostic"
    assert ServicesLogic.get_slug("IME") == "independent-medical-exams"
    assert ServicesLogic.get_slug("INFUSION") == "infusion-therapy"
    assert ServicesLogic.get_slug("PRP") == "platelet-rich-plasma-prp"
    assert ServicesLogic.get_slug("LIFESTYLE") == "lifestyle-medicine"

def test_data_id_mapping():
    # Ensure the IDs haven't been accidentally modified in code
    assert ServicesLogic.get_data_id("PAIN") == "27ecb70"
    assert ServicesLogic.get_data_id("ELECTRO") == "fc7e6d8"
    assert ServicesLogic.get_data_id("IME") == "bcabac8"
    assert ServicesLogic.get_data_id("INFUSION") == "7ce7497"
    assert ServicesLogic.get_data_id("PRP") == "b075a04"
    assert ServicesLogic.get_data_id("LIFESTYLE") == "46ea917"
    assert ServicesLogic.get_data_id("NOT_SURE") == "8279a0f"

def test_logic_returns_empty_for_invalid_key():
    assert ServicesLogic.get_slug("GHOST_KEY") == ""

