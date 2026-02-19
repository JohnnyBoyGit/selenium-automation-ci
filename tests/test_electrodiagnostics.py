import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.electrodiagnostics import ElectroDiagnosticsPage
from pages.base import BasePage

@pytest.mark.usefixtures("setup_logger")
class TestElectroDiagnosticsPage:
    def test_electrodiagnostics_page_title(self, electro_diagnostics):
        self.logger.info("--- START: ElectroDiagnostics Page Title Test ---")
        electro_diagnostics.navigate()
        assert electro_diagnostics.element_is_visible(ElectroDiagnosticsPage.ELECTRODIAG_TITLE), "ElectroDiagnostics page title is not visible"
        self.logger.info("--- FINISH: ElectroDiagnostics Page Title Test ---")

    def test_phone(self, electro_diagnostics):
        self.logger.info("--- START: Phone Test ---")
        electro_diagnostics.navigate()
        assert electro_diagnostics.element_is_visible(ElectroDiagnosticsPage.PHONE), "Phone is not visible"
        self.logger.info("--- FINISH: Phone Test ---")

    def test_address(self, electro_diagnostics):
        self.logger.info("--- START: Address Test ---")
        electro_diagnostics.navigate()
        assert electro_diagnostics.element_is_visible(ElectroDiagnosticsPage.ADDRESS), "Address is not visible"
        self.logger.info("--- FINISH: Address Test ---")

    def test_phone_icon(self, electro_diagnostics):
        self.logger.info("--- START: Phone Icon Test ---")
        electro_diagnostics.navigate()
        assert electro_diagnostics.element_is_visible(ElectroDiagnosticsPage.PHONE_ICON), "Phone icon is not visible"
        self.logger.info("--- FINISH: Phone Icon Test ---")

    def test_address_icon(self, electro_diagnostics):
        self.logger.info("--- START: Address Icon Test ---")
        electro_diagnostics.navigate()
        assert electro_diagnostics.element_is_visible(ElectroDiagnosticsPage.ADDRESS_ICON), "Address icon is not visible"
        self.logger.info("--- FINISH: Address Icon Test ---")

    def test_schedule_now_link(self, electro_diagnostics):        
        self.logger.info("--- START: ElectroDiagnostics Schedule Now Test ---")       
        electro_diagnostics.sch_now_link_flow()
        self.logger.info("--- FINISH: ElectroDiagnostics Schedule Now Test ---")

