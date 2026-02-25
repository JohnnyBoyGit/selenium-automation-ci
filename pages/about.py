from selenium.webdriver.common.by import By
from pages.base import BasePage
from src.logic.about_logic import AboutLogic

class AboutPage(BasePage):

    ABOUT_US_TITLE = (By.CSS_SELECTOR, "[data-id='53266d18'] h1")
    BUTTON_BOOK_AN_APPOINTMENT = (By.CSS_SELECTOR, "[data-id='2bb3faf1'] a")
    SCH_NOW_BUTTON = (By.CSS_SELECTOR, "[data-id='2bb3faf1'] a")

    PHONE = (By.CSS_SELECTOR, "[data-id='fff1535'] p[class='elementor-icon-box-description']")
    ADDRESS = (By.CSS_SELECTOR, "[data-id='5fcdbbf3'] h5>span")

    PHONE_ICON = (By.CSS_SELECTOR, "[data-id='fff1535'] span>i")
    ADDRESS_ICON = (By.CSS_SELECTOR, "[data-id='5fcdbbf3'] span>i")

    def __init__(self, driver):
        # Transfer the driver and wait from the parent
        super().__init__(driver)

    def navigate(self):
        self.open_url(AboutLogic.EXPECTED_PATH) # Uses the helper from BasePage


