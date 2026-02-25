# src/logic/footer_logic.py
import pytest

class FooterLogic:
    # We move the 'Truth' here. Note: Unit tests can handle the xfail marks too!
    NAV_MAP = {
        "FOOTER_SOCIAL_MEDIA_FACEBOOK": "facebook.com",
        "FOOTER_SOCIAL_MEDIA_INSTAGRAM": "instagram.com",
        "FOOTER_SOCIAL_MEDIA_GOOGLE": "Joseph+Hadi",
        "FOOTER_SOCIAL_MEDIA_TWITTER": "x.com/joehadimd",
        "FOOTER_QUICK_LINKS_SERVICES": "services",
        "FOOTER_SERVICES_PAIN_MANAGEMENT": "pain-management",
        "FOOTER_SERVICES_ELECTRODIAGNOSTICS": "electrodiagnostic",
        "FOOTER_SERVICES_IME": "independent-medical-exams",
        "FOOTER_SERVICES_PLATELET_RICH_PLASMA": "platelet-rich-plasma-prp",
        "FOOTER_SERVICES_INFUSION_THERAPY": "infusion-therapy",
        "FOOTER_SERVICES_LIFESTYLE_MEDICINE": "lifestyle-medicine",
        "FOOTER_PRIVACY_POLICY": "privacy-policy",
        "FOOTER_TERMS_AND_CONDITIONS": "terms"
    }

    # Links known to be broken (404s) - separated for clarity
    BROKEN_LINKS = {
        "FOOTER_QUICK_LINKS_ABOUT_US": "about",
        "FOOTER_QUICK_LINKS_APPOINTMENTS": "booking",
        "FOOTER_QUICK_LINKS_CONTACT_US": "contact"
    }

    @staticmethod
    def get_expected_url(key):
        return {**FooterLogic.NAV_MAP, **FooterLogic.BROKEN_LINKS}.get(key)
