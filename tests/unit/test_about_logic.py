# tests/unit/test_about_logic.py
import pytest
from src.logic.about_logic import AboutLogic

def test_about_url_mapping():
    assert AboutLogic.get_url_expectation("APPOINTMENT_LINK") == "booking"

@pytest.mark.parametrize("phone_input, expected", [
    ("(123) 456-7890", True),
    ("1234567890", True),
    ("123-456", False), # Too short
])
def test_phone_validation_logic(phone_input, expected):
    assert AboutLogic.is_valid_phone_format(phone_input) == expected

# tests/unit/test_about_logic.py
def test_address_logic():
    # Ensure the string contains what CommonLogic looks for (ENCINO or 91436)
    assert AboutLogic.is_valid_address("16255 Ventura Blvd, Encino, CA 91436") is True

