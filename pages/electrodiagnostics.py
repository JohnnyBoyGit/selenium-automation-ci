from selenium.webdriver.common.by import By
from pages.base import BasePage
from src.logic.electrodiagnostics_logic import ElectroDiagnosticsLogic

class ElectroDiagnosticsPage(BasePage):

    ELECTRODIAG_TITLE = (By.CSS_SELECTOR, "[data-id='241aaa6b'] h1")

    PHONE = (By.CSS_SELECTOR, "[data-id='27bb0090'] p[class='elementor-icon-box-description']")
    ADDRESS = (By.CSS_SELECTOR, "[data-id='472cf7a'] h5>span")

    PHONE_ICON = (By.CSS_SELECTOR, "[data-id='27bb0090'] span>i")
    ADDRESS_ICON = (By.CSS_SELECTOR, "[data-id='472cf7a'] span>i")

    SCH_NOW_BUTTON = (By.CSS_SELECTOR, "[data-id='1bc31e5'] a")

    def __init__(self, driver):
        # Transfer the driver and wait from the parent
        super().__init__(driver)

    def navigate(self):
        """Uses the Logic Layer to navigate to this page."""
        self.open_url(ElectroDiagnosticsLogic.EXPECTED_PATH)