# src/logic/services_logic.py

class ServicesLogic:

    EXPECTED_PATH = "/services"
    # Moved from the Page Object to Logic
    IMAGE_SLUGS = {
        "PAIN": "pain-management",
        "ELECTRO": "electrodiagnostic",
        "IME": "independent-medical-exams",
        "INFUSION": "infusion-therapy",
        "PRP": "platelet-rich-plasma-prp",
        "LIFESTYLE": "lifestyle-medicine"
    }

    APPOINTMENT_IDS = {
        "PAIN": "27ecb70",
        "ELECTRO": "fc7e6d8",
        "IME": "bcabac8",
        "INFUSION": "7ce7497",
        "PRP": "b075a04",
        "LIFESTYLE": "46ea917",
        "NOT_SURE": "8279a0f"
    }

    @staticmethod
    def get_slug(key):
        return ServicesLogic.IMAGE_SLUGS.get(key, "")

    @staticmethod
    def get_data_id(key):
        return ServicesLogic.APPOINTMENT_IDS.get(key, "")

    @staticmethod
    def get_all_image_keys():
        return list(ServicesLogic.IMAGE_SLUGS.keys())

    @staticmethod
    def get_all_appointment_keys():
        return list(ServicesLogic.APPOINTMENT_IDS.keys())

