from selenium.webdriver.common.by import By
from pages.base import BasePage

class ServicesPage(BasePage):

    IMAGE_DATA = {
        "PAIN": "pain-management",
        "ELECTRO": "electrodiagnostic",
        "IME": "independent-medical-exams",
        "INFUSION": "infusion-therapy",
        "PRP": "platelet-rich-plasma-prp",
        "LIFESTYLE": "lifestyle-medicine"
    }
      
    # Map semantic names to their Elementor data-ids
    APPOINTMENT_DATA = {
        "PAIN": "27ecb70",
        "ELECTRO": "fc7e6d8",
        "IME": "bcabac8",
        "INFUSION": "7ce7497",
        "PRP": "b075a04",
        "LIFESTYLE": "46ea917",
        "NOT_SURE": "8279a0f"
    }

    def __init__(self, driver):
        # Transfer the driver and wait from the parent
        super().__init__(driver)

    def navigate(self):
        """Specific navigation for this page."""
        self.open_url("/services") # Uses the helper from BasePage

    def get_appointment_locator(self, key):
        """Builds the locator dynamically using the data-id."""
        data_id = self.APPOINTMENT_DATA.get(key)
        return (By.CSS_SELECTOR, f"[data-id='{data_id}'] a")
    
    def locator_by_link_slug(self, slug):
        return (By.CSS_SELECTOR, f".elementor-widget-image a[href*='{slug}']")