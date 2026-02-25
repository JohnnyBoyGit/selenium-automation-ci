import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.contact import ContactPage
from src.logic.contact_logic import ContactLogic

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

    def test_email_link_content(self, contact):
        self.logger.info("--- START: Email Link Content Test ---")
        contact.navigate()
        assert contact.element_is_visible(ContactPage.EMAIL), "Email not visible"
        
        raw_email = contact.driver.find_element(*ContactPage.EMAIL).text
        assert ContactLogic.is_valid_email_format(raw_email), f"System error: Invalid email format '{raw_email}'"
        self.logger.info("--- FINISH: Email Link Content Test ---")
        
    def test_address_data_integrity(self, contact):
        self.logger.info("--- START: Address Data Integrity Test ---")
        contact.navigate()
        assert contact.element_is_visible(ContactPage.ADDRESS), "Address is not visible"

        raw_address = contact.driver.find_element(*ContactPage.ADDRESS).text
        assert ContactLogic.is_valid_address(raw_address), f"Wrong address displayed: {raw_address}"

        self.logger.info("--- FINISH: Address Data Integrity Test ---")

    def test_map_iframe_presence(self, contact):
        self.logger.info("--- START: Map Iframe Presence Test ---")
        contact.navigate()

        expected_part = ContactLogic.get_data("MAP_TITLE_PART")
        assert contact.element_is_visible(ContactPage.MAP_TITLE), "Map iframe not found"
        
        actual_title = contact.driver.find_element(*ContactPage.MAP_TITLE).get_attribute("title")
        assert expected_part in actual_title, f"Map title mismatch. Got: {actual_title}"

        self.logger.info("--- FINISH: Map Iframe Presence Test ---")

    def test_icons_visibility(self, contact):
        self.logger.info("--- START: Icons Visibility Test ---")
        contact.navigate()
        assert contact.element_is_visible(ContactPage.PHONE_ICON), "Phone icon is not visible"
        assert contact.element_is_visible(ContactPage.EMAIL_ICON), "Email icon is not visible"
        assert contact.element_is_visible(ContactPage.ADDRESS_ICON), "Address icon is not visible"
        self.logger.info("--- FINISH: Icons Visibility Test ---")

    