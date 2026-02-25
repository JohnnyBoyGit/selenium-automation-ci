import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.electrodiagnostics import ElectroDiagnosticsPage
from src.logic.electrodiagnostics_logic import ElectroDiagnosticsLogic
from pages.base import BasePage

@pytest.mark.usefixtures("setup_logger")
class TestElectroDiagnosticsPage:
    def test_electrodiagnostics_page_title(self, electro_diagnostics):
        self.logger.info("--- START: ElectroDiagnostics Page Title Test ---")
        electro_diagnostics.navigate()
        
        # Capture the actual text
        actual_title = electro_diagnostics.driver.find_element(*ElectroDiagnosticsPage.ELECTRODIAG_TITLE).text
        
        # Verify visibility and content
        assert electro_diagnostics.element_is_visible(ElectroDiagnosticsPage.ELECTRODIAG_TITLE)
        assert ElectroDiagnosticsLogic.EXPECTED_TITLE_PART in actual_title.upper()
        self.logger.info("--- FINISH: ElectroDiagnostics Page Title Test ---")

    def test_phone_data_integrity(self, electro_diagnostics):
        """SIT Test: Verify phone visibility and format."""
        self.logger.info("--- START: Phone Data Integrity Test ---")
        electro_diagnostics.navigate()
    
        # 1. Use your existing BasePage method to check visibility
        # This ensures the element is visible before we try to grab text
        assert electro_diagnostics.element_is_visible(ElectroDiagnosticsPage.PHONE), "Phone is not visible"
        
        # 2. Now that we know it's visible, get the text
        raw_phone = electro_diagnostics.driver.find_element(*ElectroDiagnosticsPage.PHONE).text
        
        # 3. Use the Logic Layer to verify the content
        assert ElectroDiagnosticsLogic.is_valid_phone_format(raw_phone), f"Invalid format: {raw_phone}"
        self.logger.info("--- FINISH: Phone Data Integrity Test ---")

    def test_address_data_integrity(self, electro_diagnostics):
        """SIT Test: Verify address visibility and regional accuracy."""
        self.logger.info("--- START: Address Data Integrity Test ---")
        electro_diagnostics.navigate()
        assert electro_diagnostics.element_is_visible(ElectroDiagnosticsPage.ADDRESS), "Address is not visible"
        
         # Get the raw text of the address and validate it using the Logic Layer
        raw_address = electro_diagnostics.driver.find_element(*ElectroDiagnosticsPage.ADDRESS).text
        assert ElectroDiagnosticsLogic.is_valid_address(raw_address), f"Address check failed: {raw_address}"
        self.logger.info("--- FINISH: Address Data Integrity Test ---")
  
    def test_icons_visibility(self, electro_diagnostics):
        self.logger.info("--- START: Icons Visibility Test ---")
        electro_diagnostics.navigate()
        assert electro_diagnostics.element_is_visible(ElectroDiagnosticsPage.PHONE_ICON), "Phone icon is not visible"
        assert electro_diagnostics.element_is_visible(ElectroDiagnosticsPage.ADDRESS_ICON), "Address icon is not visible"
        self.logger.info("--- FINISH: Icons Visibility Test ---")

    def test_schedule_now_link(self, electro_diagnostics):        
        self.logger.info("--- START: ElectroDiagnostics Schedule Now Test ---")       
        electro_diagnostics.sch_now_link_flow()
        self.logger.info("--- FINISH: ElectroDiagnostics Schedule Now Test ---")

