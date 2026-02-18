import pytest
from pages.pain_management import PainManagementPage

@pytest.mark.usefixtures("setup_logger")
class TestPainManagementPage:
    def test_pain_mgmt_page_title(self, pain_management):
        self.logger.info("--- START: Pain Management Page Title Test ---") 
        pain_management.navigate()
        self.logger.info("Navigated to Pain Management page.")
        assert pain_management.element_is_visible(PainManagementPage.PAIN_MGMT_TITLE), "Pain Management page title is not visible"
        self.logger.info("--- FINISH: Pain Management Page Title Test ---")

    def test_phone(self, pain_management):
        self.logger.info("--- START: Pain Management Phone Test ---") 
        pain_management.navigate()
        self.logger.info("Navigated to Pain Management page.")
        assert pain_management.element_is_visible(PainManagementPage.PHONE), "Phone is not visible"
        self.logger.info("--- FINISH: Pain Management Phone Test ---")

    def test_address(self, pain_management):
        self.logger.info("--- START: Pain Management Address Test ---") 
        pain_management.navigate()
        self.logger.info("Navigated to Pain Management page.")
        assert pain_management.element_is_visible(PainManagementPage.ADDRESS), "Address is not visible"
        self.logger.info("--- FINISH: Pain Management Address Test ---")

    def test_phone_icon(self, pain_management):
        self.logger.info("--- START: Pain Management Phone Icon Test ---") 
        pain_management.navigate()
        self.logger.info("Navigated to Pain Management page.")
        assert pain_management.element_is_visible(PainManagementPage.PHONE_ICON), "Phone icon is not visible"
        self.logger.info("--- FINISH: Pain Management Phone Icon Test ---")

    def test_address_icon(self, pain_management):
        self.logger.info("--- START: Pain Management Address Icon Test ---") 
        pain_management.navigate()
        self.logger.info("Navigated to Pain Management page.")
        assert pain_management.element_is_visible(PainManagementPage.ADDRESS_ICON), "Address icon is not visible"
        self.logger.info("--- FINISH: Pain Management Address Icon Test ---")

    def test_schedule_now_link(self, pain_management):        
        self.logger.info("--- START: Pain Management Schedule Now Test ---")       
        pain_management.sch_now_link_flow()
        self.logger.info("--- FINISH: Pain Management Schedule Now Test ---")