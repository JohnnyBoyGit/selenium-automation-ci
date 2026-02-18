import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.contact import ContactPage

@pytest.mark.usefixtures("setup_logger")
class TestContactPage:
    def test_contact_page_title(self, contact):
        self.logger.info("--- START: Contact Page Title Test ---")
        contact.navigate()
        assert contact.element_is_visible(ContactPage.CONTACT_TITLE), "Contact page title is not visible"
        self.logger.info("--- FINISH: Contact Page Title Test ---")

    def test_have_any_queries(self, contact):
        self.logger.info("--- START: Have Any Queries Test ---")
        contact.navigate()
        assert contact.element_is_visible(ContactPage.HAVE_ANY_QUERIES), "Have Any Queries is not visible"
        self.logger.info("--- FINISH: Have Any Queries Test ---")

    def test_phone_link(self, contact):
        self.logger.info("--- START: Phone Link Test ---")
        contact.navigate()
        assert contact.element_is_visible(ContactPage.PHONE), "Phone is not visible"
        self.logger.info("--- FINISH: Phone Link Test ---")

    def test_email_link(self, contact):
        self.logger.info("--- START: Email Link Test ---")
        contact.navigate()
        assert contact.element_is_visible(ContactPage.EMAIL), "Email is not visible"
        self.logger.info("--- FINISH: Email Link Test ---")
        
    def test_address(self, contact):
        self.logger.info("--- START: Address Test ---")
        contact.navigate()
        assert contact.element_is_visible(ContactPage.ADDRESS), "Address is not visible"
        self.logger.info("--- FINISH: Address Test ---")

    def test_map_title(self, contact):
        self.logger.info("--- START: Map Title Test ---")
        contact.navigate()
        assert contact.element_is_visible(ContactPage.MAP_TITLE), "Map title is not visible"
        self.logger.info("--- FINISH: Map Title Test ---")

    def test_icons_visibility(self, contact):
        self.logger.info("--- START: Icons Visibility Test ---")
        contact.navigate()
        assert contact.element_is_visible(ContactPage.PHONE_ICON), "Phone icon is not visible"
        assert contact.element_is_visible(ContactPage.EMAIL_ICON), "Email icon is not visible"
        assert contact.element_is_visible(ContactPage.ADDRESS_ICON), "Address icon is not visible"
        self.logger.info("--- FINISH: Icons Visibility Test ---")

    