import pytest
from pages.pain_management import PainManagementPage
from src.logic.pain_management_logic import PainManagementLogic
from src.logic.common_logic import CommonLogic

@pytest.mark.usefixtures("setup_logger")
class TestPainManagementPage:

    def test_pain_mgmt_page_title(self, pain_management):
        self.logger.info("--- START: Pain Management Page Title Test ---") 
        pain_management.navigate()

        self.logger.info("Navigated to Pain Management page.")

         # 1. Visibility Check (Defensive)
        assert pain_management.element_is_visible(pain_management.PAIN_MGMT_TITLE), "Title not visible"
        
        # 2. Content Check (Logic Layer)
        actual_title = pain_management.driver.find_element(*pain_management.PAIN_MGMT_TITLE).text
        assert PainManagementLogic.EXPECTED_TITLE_PART in actual_title.upper(), f"Title mismatch: {actual_title}"
        
        self.logger.info("--- FINISH: Pain Management Page Title Test ---")


    def test_phone(self, pain_management):
        self.logger.info("--- START: Pain Management Phone Test ---") 
        pain_management.navigate()

        self.logger.info("Navigated to Pain Management page.")

        # Defensive Check
        assert pain_management.element_is_visible(pain_management.PHONE), "Phone element not visible"
        
        # Data Integrity Check
        raw_phone = pain_management.driver.find_element(*pain_management.PHONE).text
        assert PainManagementLogic.is_valid_phone_format(raw_phone), f"Invalid phone format: {raw_phone}"

        self.logger.info("--- FINISH: Pain Management Phone Test ---")


    def test_address(self, pain_management):
        self.logger.info("--- START: Pain Management Address Test ---") 
        pain_management.navigate()
        self.logger.info("Navigated to Pain Management page.")

        # Defensive Check
        assert pain_management.element_is_visible(pain_management.ADDRESS), "Address element not visible"
        
        # Regional Check (Encino/Zip)
        raw_address = pain_management.driver.find_element(*pain_management.ADDRESS).text
        assert PainManagementLogic.is_valid_address(raw_address), f"Address check failed: {raw_address}"

        self.logger.info("--- FINISH: Pain Management Address Test ---")


    def test_icon_visibility(self, pain_management):
        self.logger.info("--- START: Pain Management Icon Visibility Test ---") 
        pain_management.navigate()
        self.logger.info("Navigated to Pain Management page.")
        assert pain_management.element_is_visible(pain_management.PHONE_ICON), "Phone icon is not visible"
        assert pain_management.element_is_visible(pain_management.ADDRESS_ICON), "Address icon is not visible"
        self.logger.info("--- FINISH: Pain Management Icon Visibility Test ---")


    def test_schedule_now_link(self, pain_management):        
        self.logger.info("--- START: Pain Management Schedule Now Test ---")       
        CommonLogic.verify_link_flow(page=pain_management, locator=pain_management.SCH_NOW_BUTTON, expected_slug="booking", click_type="safe", scroll=True)
        self.logger.info("--- FINISH: Pain Management Schedule Now Test ---")