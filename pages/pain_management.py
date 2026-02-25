from selenium.webdriver.common.by import By
from pages.base import BasePage
from src.logic.pain_management_logic import PainManagementLogic

class PainManagementPage(BasePage):

    PAIN_MGMT_TITLE = (By.CSS_SELECTOR, "[data-id='1812064a'] h1")

    PHONE = (By.CSS_SELECTOR, "[data-id='6a0cfdfe'] p[class='elementor-icon-box-description']")
    ADDRESS = (By.CSS_SELECTOR, "[data-id='305f508b'] h5>span")

    PHONE_ICON = (By.CSS_SELECTOR, "[data-id='6a0cfdfe'] span>i")
    ADDRESS_ICON = (By.CSS_SELECTOR, "[data-id='305f508b'] span>i")

    SCH_NOW_BUTTON = (By.CSS_SELECTOR, "[data-id='7b727d07'] a")

    def __init__(self, driver):
        # Transfer the driver and wait from the parent
        super().__init__(driver)

    def navigate(self):
        """Uses the Logic Layer to navigate to this page."""
        self.open_url(PainManagementLogic.EXPECTED_PATH)