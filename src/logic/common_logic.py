# src/logic/common_logic.py

class CommonLogic:
    @staticmethod
    def is_valid_phone_format(phone_text):
        """Standard verification for all phone numbers across the site."""
        clean_phone = "".join(filter(str.isdigit, phone_text))
        return len(clean_phone) >= 10

    @staticmethod
    def is_valid_address(address_text):
        """Standard check for regional office data (Encino/91436)."""
        address_upper = address_text.upper()
        return "91436" in address_upper or "ENCINO" in address_upper
