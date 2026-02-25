# tests/unit/test_contact_logic.py
import pytest
from src.logic.contact_logic import ContactLogic

def test_email_validation_logic():
    assert ContactLogic.is_valid_email_format("info@calipain.com") is True
    assert ContactLogic.is_valid_email_format("invalid-email") is False

def test_address_validation_logic():
    # Change 'is_valid_address_snippet' to 'is_valid_address'
    assert ContactLogic.is_valid_address("Encino, CA 91436") is True
