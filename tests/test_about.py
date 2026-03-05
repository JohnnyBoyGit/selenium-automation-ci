import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.about import AboutPage
from src.logic.about_logic import AboutLogic
from src.logic.common_logic import CommonLogic

@pytest.mark.usefixtures("setup_logger")
class TestAboutPage:
    
    def test_about_us_title(self, about):
        self.logger.info("--- START: About Us Title Test ---")
        about.navigate()
        assert about.element_is_visible(about.ABOUT_US_TITLE), "About Us title is not visible"
        self.logger.info("--- FINISH: About Us Title Test ---")


    def test_phone_visibility_and_format(self, about):
        self.logger.info("--- START: Phone Visibility & Format Test ---")
        about.navigate()
        
        # 1. Check Visibility (Your original check)
        assert about.element_is_visible(about.PHONE), "Phone element not visible"
        
        # 2. Check Content (The new "Senior" check)
        raw_text = about.driver.find_element(*about.PHONE).text
        assert AboutLogic.is_valid_phone_format(raw_text), f"Phone text '{raw_text}' is not a valid format"
        
        self.logger.info("Phone visibility and format verified.")

        self.logger.info("--- FINISH: Phone Visibility & Format Test ---")


    def test_address_visibility_and_validation(self, about):
        self.logger.info("--- START: About Us Address Visibility & Validation Test ---")
        about.navigate()

        assert about.element_is_visible(about.ADDRESS), "Address is not visible"

        raw_text = about.driver.find_element(*about.ADDRESS).text
        assert AboutLogic.is_valid_address(raw_text), f"Address text '{raw_text}' does not appear valid"
        
        self.logger.info("Address visibility and validation verified.")
        
        self.logger.info("--- FINISH: About Us Address Visibility & Validation Test ---")


    def test_phone_icon(self, about):
        self.logger.info("--- START: About Us Phone Icon Test ---")
        about.navigate()
        assert about.element_is_visible(about.PHONE_ICON), "Phone icon is not visible"
        self.logger.info("--- FINISH: About Us Phone Icon Test ---")


    def test_address_icon(self, about):
        self.logger.info("--- START: About Us Address Icon Test ---")
        about.navigate()
        assert about.element_is_visible(about.ADDRESS_ICON), "Address icon is not visible"
        self.logger.info("--- FINISH: About Us Address Icon Test ---")


    def test_appointment_link(self, about):
        self.logger.info("--- START: About Us Appointment Link Test ---")
        CommonLogic.verify_link_flow(page=about, locator=about.BUTTON_BOOK_AN_APPOINTMENT, expected_slug="booking", click_type="force", scroll=True)
        self.logger.info("--- FINISH: About Us Appointment Link Test ---")


    def test_schedule_now_link(self, about):        
        self.logger.info("--- START: About Us Schedule Now Test ---")       
        CommonLogic.verify_link_flow(page=about, locator=about.SCH_NOW_BUTTON, expected_slug="booking", click_type="safe", scroll=True)
        self.logger.info("--- FINISH: About Us Schedule Now Test ---")

    