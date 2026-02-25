from selenium.webdriver.common.by import By
from pages.base import BasePage
from src.logic.contact_logic import ContactLogic

class ContactPage(BasePage):

    CONTACT_TITLE = (By.CSS_SELECTOR, "[data-id='849e935'] h1")
    HAVE_ANY_QUERIES = (By.CSS_SELECTOR, "[data-id='09e6ff8'] h2")
    PHONE = (By.CSS_SELECTOR, "[data-id='6ce4e76'] h4>span")
    EMAIL = (By.CSS_SELECTOR, "[data-id='fae7bd6'] h4>span")
    ADDRESS = (By.CSS_SELECTOR, "[data-id='86ee224'] h4>span")
    MAP_TITLE = (By.CSS_SELECTOR, "[data-id='807864a'] iframe[title='16255 Ventura Blvd, Encino, CA 91436']")

    PHONE_ICON = (By.CSS_SELECTOR, "[data-id='6ce4e76'] .fas.fa-phone-alt")
    EMAIL_ICON = (By.CSS_SELECTOR, "[data-id='fae7bd6'] .fas.fa-envelope")
    ADDRESS_ICON = (By.CSS_SELECTOR, "[data-id='86ee224'] .fas.fa-map-marker-alt")

    def __init__(self, driver):
        # Transfer the driver and wait from the parent
        super().__init__(driver)

    def navigate(self):
        """Uses the Logic Layer to navigate home."""
        self.open_url(ContactLogic.EXPECTED_PATH) 