# tests/unit/test_footer_logic.py
import pytest
from src.logic.footer_logic import FooterLogic

def test_footer_nav_mapping():
    # Test a few critical social and service links
    assert FooterLogic.get_expected_url("FOOTER_SOCIAL_MEDIA_FACEBOOK") == "facebook.com"
    assert FooterLogic.get_expected_url("FOOTER_SERVICES_PAIN_MANAGEMENT") == "pain-management"
    assert FooterLogic.get_expected_url("FOOTER_PRIVACY_POLICY") == "privacy-policy"

def test_footer_broken_links_mapping():
    # Verify the broken links are still mapped to their intended slugs
    # This ensures that once the site is fixed, our expectation is already set
    assert FooterLogic.get_expected_url("FOOTER_QUICK_LINKS_ABOUT_US") == "about"
    assert FooterLogic.get_expected_url("FOOTER_QUICK_LINKS_CONTACT_US") == "contact"

def test_invalid_footer_key():
    assert FooterLogic.get_expected_url("NON_EXISTENT_LINK") is None
