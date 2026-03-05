import pytest
from pages.prp import PrpPage
from src.logic.prp_logic import PrpLogic
from src.logic.common_logic import CommonLogic

@pytest.mark.usefixtures("setup_logger")
class TestPrpPage:  # Platelet-Rich Plasma Page

    def test_prp_page_title_and_content(self, prp):
        self.logger.info("--- START: PRP Page Title Test ---") 
        prp.navigate()

        self.logger.info("Navigated to PRP page.")

        # 1. Visibility Check (Defensive) - No * needed for your helper
        assert prp.element_is_visible(prp.PRP_TITLE), "PRP title not visible"
        
        # 2. Content Check (SIT) - * is needed for native find_element
        actual_title = prp.driver.find_element(*prp.PRP_TITLE).text
        assert PrpLogic.EXPECTED_TITLE_PART in actual_title.upper(), f"Title mismatch: {actual_title}"
        self.logger.info("--- FINISH: PRP Page Title Test ---")


    def test_phone_data_integrity(self, prp):
        self.logger.info("--- START: PRP Phone Test ---") 
        prp.navigate()
        self.logger.info("Navigated to PRP page.")

        assert prp.element_is_visible(prp.PHONE), "Phone is not visible"

        raw_phone = prp.driver.find_element(*prp.PHONE).text
        assert PrpLogic.is_valid_phone_format(raw_phone), f"Invalid phone: {raw_phone}"

        self.logger.info("--- FINISH: PRP Phone Test ---")


    def test_address(self, prp):
        self.logger.info("--- START: PRP Address Test ---") 
        prp.navigate()
        self.logger.info("Navigated to PRP page.")

        assert prp.element_is_visible(prp.ADDRESS), "Address is not visible"

        raw_address = prp.driver.find_element(*prp.ADDRESS).text
        assert PrpLogic.is_valid_address(raw_address), f"Address mismatch: {raw_address}"

        self.logger.info("--- FINISH: PRP Address Test ---")


    def test_icons_visibility(self, prp):
        self.logger.info("--- START: PRP Icons Visibility Test ---") 
        prp.navigate()
        self.logger.info("Navigated to PRP page.")
        assert prp.element_is_visible(prp.PHONE_ICON), "Phone icon is not visible"
        assert prp.element_is_visible(prp.ADDRESS_ICON), "Address icon is not visible"
        self.logger.info("--- FINISH: PRP Icons Visibility Test ---")


    def test_schedule_now_link(self, prp): 
        self.logger.info("--- START: PRP Schedule Now Test ---")       
        CommonLogic.verify_link_flow(page=prp, locator=prp.SCH_NOW_BUTTON, expected_slug="booking", click_type="safe", scroll=True)
        self.logger.info("--- FINISH: PRP Schedule Now Test ---")