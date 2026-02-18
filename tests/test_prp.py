import pytest
from pages.prp import PrpPage

@pytest.mark.usefixtures("setup_logger")
class TestPrpPage:  # Platelet-Rich Plasma Page
    def test_prp_page_title(self, prp):
        self.logger.info("--- START: PRP Page Title Test ---") 
        prp.navigate()
        self.logger.info("Navigated to PRP page.")
        assert prp.element_is_visible(PrpPage.PRP_TITLE), "Platelet-Rich Plasma page title is not visible"
        self.logger.info("--- FINISH: PRP Page Title Test ---")

    def test_phone(self, prp):
        self.logger.info("--- START: PRP Phone Test ---") 
        prp.navigate()
        self.logger.info("Navigated to PRP page.")
        assert prp.element_is_visible(PrpPage.PHONE), "Phone is not visible"
        self.logger.info("--- FINISH: PRP Phone Test ---")

    def test_address(self, prp):
        self.logger.info("--- START: PRP Address Test ---") 
        prp.navigate()
        self.logger.info("Navigated to PRP page.")
        assert prp.element_is_visible(PrpPage.ADDRESS), "Address is not visible"
        self.logger.info("--- FINISH: PRP Address Test ---")

    def test_phone_icon(self, prp):
        self.logger.info("--- START: PRP Phone Icon Test ---") 
        prp.navigate()
        self.logger.info("Navigated to PRP page.")
        assert prp.element_is_visible(PrpPage.PHONE_ICON), "Phone icon is not visible"
        self.logger.info("--- FINISH: PRP Phone Icon Test ---")

    def test_address_icon(self, prp):
        self.logger.info("--- START: PRP Address Icon Test ---") 
        prp.navigate()
        self.logger.info("Navigated to PRP page.")
        assert prp.element_is_visible(PrpPage.ADDRESS_ICON), "Address icon is not visible"
        self.logger.info("--- FINISH: PRP Address Icon Test ---")

    def test_schedule_now_link(self, prp): 
        self.logger.info("--- START: PRP Schedule Now Test ---")       
        prp.sch_now_link_flow()
        self.logger.info("--- FINISH: PRP Schedule Now Test ---")