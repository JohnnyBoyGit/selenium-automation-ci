# tests/unit/test_home_logic.py
import pytest
from src.logic.home_logic import HomeLogic

def test_home_url_mapping():
    """Verify that specific buttons point to the correct internal slugs."""
    assert HomeLogic.get_url_expectation("BUTTON_READ_ME") == "about"
    assert HomeLogic.get_url_expectation("BUTTON_VIEW_ALL_SERVICES") == "services"

@pytest.mark.parametrize("button_key, expected_slug", [
    ("BUTTON_BOOK_AN_APPOINTMENT_1", "booking"),
    ("BUTTON_SCHEDULE_NOW", "booking"),
])
def test_appointment_button_mapping(button_key, expected_slug):
    """Senior Tip: Use parametrization to test multiple button mappings at once."""
    assert HomeLogic.get_url_expectation(button_key) == expected_slug

def test_rating_validation_logic():
    """Verify the logic that determines if a TrustIndex rating is 'Excellent'."""
    # Test True cases
    assert HomeLogic.is_rating_valid("Our rating is EXCELLENT!") is True
    assert HomeLogic.is_rating_valid("excellent") is True  # Should be case-insensitive
    
    # Test False cases
    assert HomeLogic.is_rating_valid("Good") is False
    assert HomeLogic.is_rating_valid("") is False

def test_home_path_constant():
    """Ensure the base path is correctly defined as an empty string (Home)."""
    assert HomeLogic.EXPECTED_PATH == ""
