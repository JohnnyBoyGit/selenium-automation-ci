# tests/unit/test_header_logic.py
from src.logic.header_logic import HeaderLogic

def test_header_main_nav_mapping():
    assert HeaderLogic.get_expected_url("SITE_LOGO") == "calipain.com"
    assert HeaderLogic.get_expected_url("ABOUT_MENU_ITEM") == "/about"
    assert HeaderLogic.get_expected_url("CONTACT_MENU_ITEM") == "/contact"

def test_header_submenu_mapping():
    # Verify the specialized service slugs in the submenu
    assert HeaderLogic.get_expected_url("SERVICES_SUBMENU_ELECTRODIAGNOSTICS") == "electrodiagnostic"
    assert HeaderLogic.get_expected_url("SERVICES_SUBMENU_LIFESTYLE_MEDICINE") == "lifestyle-medicine"
