import pytest
from pages.ime import ImePage

@pytest.mark.usefixtures("setup_logger")
class TestImePage:  # Independent Medical Exams Page
    def test_ime_page_title(self, ime):
        self.logger.info("--- START: Ime Page Title Test ---")
        ime.navigate()
        assert ime.element_is_visible(ImePage.IME_TITLE), "Independent Medical Exams page title is not visible"
        self.logger.info("--- FINISH: Ime Page Title Test ---")

    def test_phone(self, ime):
        self.logger.info("--- START: Phone Test ---")
        ime.navigate()
        assert ime.element_is_visible(ImePage.PHONE), "Phone is not visible"
        self.logger.info("--- FINISH: Phone Test ---")

    def test_address(self, ime):
        self.logger.info("--- START: Address Test ---")
        ime.navigate()
        assert ime.element_is_visible(ImePage.ADDRESS), "Address is not visible"
        self.logger.info("--- FINISH: Address Test ---")

    def test_phone_icon(self, ime):
        self.logger.info("--- START: Phone Icon Test ---")
        ime.navigate()
        assert ime.element_is_visible(ImePage.PHONE_ICON), "Phone icon is not visible"
        self.logger.info("--- FINISH: Phone Icon Test ---")

    def test_address_icon(self, ime):
        self.logger.info("--- START: Address Icon Test ---")
        ime.navigate()
        assert ime.element_is_visible(ImePage.ADDRESS_ICON), "Address icon is not visible"
        self.logger.info("--- FINISH: Address Icon Test ---")

    def test_schedule_now_link(self, ime):        
        self.logger.info("--- START: Schedule Now Test ---")       
        ime.sch_now_link_flow()
        self.logger.info("--- FINISH: Schedule Now Test ---")
