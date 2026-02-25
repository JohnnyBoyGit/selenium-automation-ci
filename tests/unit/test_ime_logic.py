# pages/ime.py
from selenium.webdriver.common.by import By
from pages.base import BasePage
from src.logic.ime_logic import ImeLogic

class ImePage(BasePage):
    # ... (Your locators stay exactly as they are) ...

    def navigate(self):
        """Uses the Logic Layer to navigate to the current correct URL."""
        self.open_url(ImeLogic.EXPECTED_PATH)
