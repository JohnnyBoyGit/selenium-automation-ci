from selenium.webdriver.common.by import By
from pages.base import BasePage
from src.logic.prp_logic import PrpLogic

class PrpPage(BasePage):    # Platelet-Rich Plasma Page

    PRP_TITLE = (By.CSS_SELECTOR, "[data-id='aea0209'] h1")

    PHONE = (By.CSS_SELECTOR, "[data-id='49a55c59'] p[class='elementor-icon-box-description']")
    ADDRESS = (By.CSS_SELECTOR, "[data-id='1789d772'] h5>span")

    PHONE_ICON = (By.CSS_SELECTOR, "[data-id='49a55c59'] span>i")
    ADDRESS_ICON = (By.CSS_SELECTOR, "[data-id='1789d772'] span>i")

    SCH_NOW_BUTTON = (By.CSS_SELECTOR, "[data-id='5573bb85'] a")

    def __init__(self, driver):
        # Transfer the driver and wait from the parent
        super().__init__(driver)


    def navigate(self):
        # Use the logic layer for the path
        self.open_url(PrpLogic.EXPECTED_PATH)