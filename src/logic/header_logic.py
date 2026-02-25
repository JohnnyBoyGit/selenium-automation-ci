# src/logic/header_logic.py

class HeaderLogic:
    NAV_MAP = {
        "SITE_LOGO": "calipain.com",
        "HOME_MENU_ITEM": "calipain.com",
        "ABOUT_MENU_ITEM": "/about",
        "SERVICES_MENU_ITEM": "/services",
        "CONTACT_MENU_ITEM": "/contact",
        "SERVICES_SUBMENU_PAIN_MANAGEMENT": "pain-management",
        "SERVICES_SUBMENU_ELECTRODIAGNOSTICS": "electrodiagnostic",
        "SERVICES_SUBMENU_INDEPENDENT_MEDICAL_EXAMS": "independent-medical-exams",
        "SERVICES_SUBMENU_INFUSION_THERAPY": "infusion-therapy",
        "SERVICES_SUBMENU_PLATELET_RICH_PLASMA_PRP": "platelet-rich-plasma-prp",
        "SERVICES_SUBMENU_LIFESTYLE_MEDICINE": "lifestyle-medicine"
    }

    @staticmethod
    def get_expected_url(key):
        return HeaderLogic.NAV_MAP.get(key)
