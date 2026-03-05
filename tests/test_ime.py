import pytest
from pages.ime import ImePage
from src.logic.ime_logic import ImeLogic
from src.logic.common_logic import CommonLogic

@pytest.mark.usefixtures("setup_logger")
class TestImePage:  # Independent Medical Exams Page
    
    def test_ime_page_title(self, ime):
        self.logger.info("--- START: Ime Page Title Test ---")
        ime.navigate()
        self.logger.info("Navigated to IME page.")

        # 1. Visibility Check (Functional)
        assert ime.element_is_visible(ime.IME_TITLE), "IME Title not visible"
        
        # 2. Content Check (SIT)
        actual_title = ime.driver.find_element(*ime.IME_TITLE).text
        assert ImeLogic.EXPECTED_TITLE_PART in actual_title.upper(), f"Title mismatch: {actual_title}"
        self.logger.info("--- FINISH: IME Page Title Test ---")


    def test_phone_data_integrity(self, ime):
        self.logger.info("--- START: Phone Test ---")
        ime.navigate()
        self.logger.info("Navigated to IME page.")

        assert ime.element_is_visible(ime.PHONE), "Phone is not visible"

        raw_phone = ime.driver.find_element(*ime.PHONE).text
        assert ImeLogic.is_valid_phone_format(raw_phone), f"Invalid phone format: {raw_phone}"

        self.logger.info("--- FINISH: Phone Test ---")


    def test_address_data_integrity(self, ime):
        self.logger.info("--- START: Address Test ---")
        ime.navigate()
        self.logger.info("Navigated to IME page.")

        assert ime.element_is_visible(ime.ADDRESS), "Address is not visible"

        raw_address = ime.driver.find_element(*ime.ADDRESS).text
        assert ImeLogic.is_valid_address(raw_address), f"Address check failed: {raw_address}"

        self.logger.info("--- FINISH: Address Test ---")


    def test_icons_visibility(self, ime):
        self.logger.info("--- START: Icons Visibility Test ---")
        ime.navigate()
        assert ime.element_is_visible(ime.PHONE_ICON), "Phone icon is not visible"
        assert ime.element_is_visible(ime.ADDRESS_ICON), "Address icon is not visible"
        self.logger.info("--- FINISH: Icons Visibility Test ---")


    def test_schedule_now_link(self, ime):        
        self.logger.info("--- START: Schedule Now Test ---")       
        CommonLogic.verify_link_flow(page=ime, locator=ime.SCH_NOW_BUTTON, expected_slug="booking", click_type="safe", scroll=True)
        self.logger.info("--- FINISH: Schedule Now Test ---")
