from selenium.webdriver.common.by import By
from pages.base import BasePage

class InfusionTherapyPage(BasePage):

    INFUSION_TITLE = (By.CSS_SELECTOR, "[data-id='3ece6fe2'] h1")

    PHONE = (By.CSS_SELECTOR, "[data-id='1a4a9ed7'] p[class='elementor-icon-box-description']")
    ADDRESS = (By.CSS_SELECTOR, "[data-id='4f8c4c5e'] h5>span")

    PHONE_ICON = (By.CSS_SELECTOR, "[data-id='1a4a9ed7'] span>i")
    ADDRESS_ICON = (By.CSS_SELECTOR, "[data-id='4f8c4c5e'] span>i")

    SCH_NOW_BUTTON = (By.CSS_SELECTOR, "[data-id='6dee0153'] a")

    def __init__(self, driver):
        # Transfer the driver and wait from the parent
        super().__init__(driver)

    def navigate(self):
        """Specific navigation for this page."""
        self.open_url("/infusion-therapy-2") # Uses the helper from BasePage