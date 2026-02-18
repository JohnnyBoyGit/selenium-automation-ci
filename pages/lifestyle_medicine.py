from selenium.webdriver.common.by import By
from pages.base import BasePage

class LifestyleMedicinePage(BasePage):    # Lifestyle Medicine Page

    LIFESTYLE_MEDICINE_TITLE = (By.CSS_SELECTOR, "[data-id='475a9b1a'] h1")
    IV_THERAPY_SERVICES = (By.CSS_SELECTOR, "[data-id='e1491d0'] a")

    HAIR_RESTORATION = (By.ID, "elementor-tab-title-1531")
    REVITALIZE = (By.ID, "elementor-tab-title-1532")

    HAIR_RESTORATION_CONTENT = (By.ID, "elementor-tab-content-1531")
    REVITALIZE_CONTENT = (By.ID, "elementor-tab-content-1532")

    HAIR_RESTORATION_CONTENT_LINK = (By.CSS_SELECTOR, "[id='elementor-tab-content-1531'] p>a")
    REVITALIZE_CONTENT_LINK = (By.CSS_SELECTOR, "[id='elementor-tab-content-1532'] a")

    PHONE = (By.CSS_SELECTOR, "[data-id='55e6c8b9'] p[class='elementor-icon-box-description']")
    ADDRESS = (By.CSS_SELECTOR, "[data-id='612de6c3'] h5>span")

    PHONE_ICON = (By.CSS_SELECTOR, "[data-id='55e6c8b9'] span>i")
    ADDRESS_ICON = (By.CSS_SELECTOR, "[data-id='612de6c3'] span>i")

    SCH_NOW_BUTTON = (By.CSS_SELECTOR, "[data-id='6175a395'] a")

    def __init__(self, driver):
        # Transfer the driver and wait from the parent
        super().__init__(driver)

    def navigate(self):
        """Specific navigation for this page."""
        self.open_url("/lifestyle-medicine-2") # Uses the helper from BasePage