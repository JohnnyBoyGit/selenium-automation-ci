from selenium.webdriver.common.by import By
from pages.base import BasePage

class ImePage(BasePage):

    IME_TITLE = (By.CSS_SELECTOR, "[data-id='137fb0e1'] h1")

    PHONE = (By.CSS_SELECTOR, "[data-id='4cb944bd'] p[class='elementor-icon-box-description']")
    ADDRESS = (By.CSS_SELECTOR, "[data-id='11598fd4'] h5>span")

    PHONE_ICON = (By.CSS_SELECTOR, "[data-id='4cb944bd'] span>i")
    ADDRESS_ICON = (By.CSS_SELECTOR, "[data-id='11598fd4'] span>i")

    SCH_NOW_BUTTON = (By.CSS_SELECTOR, "[data-id='3400fa7a'] a")

    def __init__(self, driver):
        # Transfer the driver and wait from the parent
        super().__init__(driver)

    def navigate(self):
        """Specific navigation for this page."""
        self.open_url("/independent-medical-exams-2") # Uses the helper from BasePage