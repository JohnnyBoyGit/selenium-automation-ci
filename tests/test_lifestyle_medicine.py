from pages.lifestyle_medicine import LifestyleMedicinePage
import pytest
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.usefixtures("setup_logger")
class TestLifestyleMedicinePage:  # Lifestyle Medicine Page
    def test_lifestyle_medicine_page_title(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine Page Title Test ---")
        lifestyle_medicine.navigate()
        assert lifestyle_medicine.element_is_visible(LifestyleMedicinePage.LIFESTYLE_MEDICINE_TITLE), "Lifestyle Medicine page title is not visible"

    def test_iv_therapy_services_link(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine IV Therapy Services Link Test ---")
        lifestyle_medicine.navigate() 
        self.logger.info("Navigated to Lifestyle Medicine page.")

        locator = lifestyle_medicine.IV_THERAPY_SERVICES
        assert lifestyle_medicine.element_is_visible(locator), "IV Therapy Services link is not visible"

        expected_url = "infusion-therapy"

        self.logger.info(f"Clicking IV Therapy Services link with force_click: {locator}")
        lifestyle_medicine.force_click(locator)

        self.logger.info("Handling external tab if opened...")
        lifestyle_medicine.handle_external_tab()
        
        try:
            # 2026 Tip: URL waits are more stable than raw asserts
            lifestyle_medicine.wait.until(EC.url_contains(expected_url))
        except:
            actual = lifestyle_medicine.driver.current_url
            pytest.fail(f"Link {locator} failed. Expected slug '{expected_url}' but got '{actual}'")
        
        # Cleanup tabs
        if len(lifestyle_medicine.driver.window_handles) > 1:
            self.logger.info("Closing external tab.")
            lifestyle_medicine.driver.close()

            lifestyle_medicine.driver.switch_to.window(lifestyle_medicine.driver.window_handles[0])
            self.logger.info("Switched back to original tab.")

        self.logger.info("--- FINISH: Lifestyle Medicine IV Therapy Services Link Test ---")

    def test_hair_restoration_link(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine Hair Restoration Link Test ---")
        lifestyle_medicine.navigate()
        locator = lifestyle_medicine.HAIR_RESTORATION
        assert lifestyle_medicine.element_is_visible(locator), "Hair Restoration link is not visible"
        self.logger.info("--- FINISH: Lifestyle Medicine Hair Restoration Link Test ---")

    def test_toggle_hair_restoration_content(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine Toggle Hair Restoration Content Test ---")
        lifestyle_medicine.navigate()
        self.logger.info("Navigated to Lifestyle Medicine page.")

        self.logger.info("Clicking Hair Restoration link to show content.")
        lifestyle_medicine.force_click(lifestyle_medicine.HAIR_RESTORATION)
        assert lifestyle_medicine.element_is_visible(LifestyleMedicinePage.HAIR_RESTORATION_CONTENT), "Hair Restoration content is not visible"
        
        self.logger.info("Clicking Hair Restoration link again to hide content.")
        lifestyle_medicine.force_click(lifestyle_medicine.HAIR_RESTORATION)
        assert lifestyle_medicine.element_is_visible(lifestyle_medicine.HAIR_RESTORATION), "Hair Restoration link is not visible"
        self.logger.info("--- FINISH: Lifestyle Medicine Toggle Hair Restoration Content Test ---")

    def test_hair_restoration_content_link(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine Hair Restoration Content Link Test ---")
        lifestyle_medicine.navigate()
        self.logger.info("Navigated to Lifestyle Medicine page.")

        self.logger.info("Clicking Hair Restoration link to show content.")
        lifestyle_medicine.force_click(lifestyle_medicine.HAIR_RESTORATION)
        assert lifestyle_medicine.element_is_visible(LifestyleMedicinePage.HAIR_RESTORATION_CONTENT), "Hair Restoration content is not visible"
        

        expected_url = "platelet-rich-plasma-prp"
        prp_locator = lifestyle_medicine.HAIR_RESTORATION_CONTENT_LINK
        self.logger.info(f"Clicking Hair Restoration content link with force_click: {prp_locator}")
        lifestyle_medicine.force_click(prp_locator)
        
        self.logger.info("Handling external tab if opened...")
        lifestyle_medicine.handle_external_tab()
        
        try:
            # 2026 Tip: URL waits are more stable than raw asserts
            lifestyle_medicine.wait.until(EC.url_contains(expected_url))
        except:
            actual = lifestyle_medicine.driver.current_url
            pytest.fail(f"Link {prp_locator} failed. Expected slug '{expected_url}' but got '{actual}'")
        
        # Cleanup tabs
        if len(lifestyle_medicine.driver.window_handles) > 1:
            self.logger.info("Closing external tab.")
            lifestyle_medicine.driver.close()
            lifestyle_medicine.driver.switch_to.window(lifestyle_medicine.driver.window_handles[0])
            self.logger.info("Switched back to original tab.")

        self.logger.info("--- FINISH: Lifestyle Medicine Hair Restoration Content Link Test ---")

    def test_hair_revitalize_link(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine Hair Revitalize Link Test ---")
        lifestyle_medicine.navigate()
        self.logger.info("Navigated to Lifestyle Medicine page.")

        locator = lifestyle_medicine.REVITALIZE
        assert lifestyle_medicine.element_is_visible(locator), "Revitalize link is not visible"
        self.logger.info("--- FINISH: Lifestyle Medicine Hair Revitalize Link Test ---")

    def test_toggle_revitalize_content(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine Toggle Revitalize Content Test ---")
        lifestyle_medicine.navigate()
        self.logger.info("Navigated to Lifestyle Medicine page.")
        
        self.logger.info("Clicking Revitalize link to show content.")
        lifestyle_medicine.force_click(lifestyle_medicine.REVITALIZE)
        assert lifestyle_medicine.element_is_visible(LifestyleMedicinePage.REVITALIZE_CONTENT), "Revitalize content is not visible"
        self.logger.info("Clicking Revitalize link again to hide content.")
        lifestyle_medicine.force_click(lifestyle_medicine.REVITALIZE)
        self.logger.info("--- FINISH: Lifestyle Medicine Toggle Revitalize Content Test ---")

    def test_revitalize_content_link(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine Revitalize Content Link Test ---")
        lifestyle_medicine.navigate()
        self.logger.info("Navigated to Lifestyle Medicine page.")
        
        self.logger.info("Clicking Revitalize link to show content.")
        lifestyle_medicine.force_click(lifestyle_medicine.REVITALIZE)
        assert lifestyle_medicine.element_is_visible(LifestyleMedicinePage.REVITALIZE_CONTENT), "Revitalize content is not visible"

        expected_url = "infusion-therapy"
        iv_locator = lifestyle_medicine.REVITALIZE_CONTENT_LINK
        self.logger.info(f"Clicking Revitalize content link with force_click: {iv_locator}")
        lifestyle_medicine.force_click(iv_locator)
        time.sleep(2)  # Wait for the new tab to open
        lifestyle_medicine.handle_external_tab()
        self.logger.info("Handling external tab if opened...")

        try:
            # 2026 Tip: URL waits are more stable than raw asserts
            lifestyle_medicine.wait.until(EC.url_contains(expected_url))
        except:
            actual = lifestyle_medicine.driver.current_url
            pytest.fail(f"Link {iv_locator} failed. Expected slug '{expected_url}' but got '{actual}'")
        
        # Cleanup tabs
        if len(lifestyle_medicine.driver.window_handles) > 1:
            self.logger.info("Closing external tab.")
            lifestyle_medicine.driver.close()
            lifestyle_medicine.driver.switch_to.window(lifestyle_medicine.driver.window_handles[0])
            self.logger.info("Switched back to original tab.")

        self.logger.info("--- FINISH: Lifestyle Medicine Revitalize Content Link Test ---")

    def test_phone(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine Phone Test ---")
        lifestyle_medicine.navigate()
        assert lifestyle_medicine.element_is_visible(LifestyleMedicinePage.PHONE), "Phone is not visible"
        self.logger.info("--- FINISH: Lifestyle Medicine Phone Test ---")

    def test_address(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine Address Test ---")
        lifestyle_medicine.navigate()
        assert lifestyle_medicine.element_is_visible(LifestyleMedicinePage.ADDRESS), "Address is not visible"
        self.logger.info("--- FINISH: Lifestyle Medicine Address Test ---")

    def test_phone_icon(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine Phone Icon Test ---")
        lifestyle_medicine.navigate()
        assert lifestyle_medicine.element_is_visible(LifestyleMedicinePage.PHONE_ICON), "Phone icon is not visible"
        self.logger.info("--- FINISH: Lifestyle Medicine Phone Icon Test ---")

    def test_address_icon(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine Address Icon Test ---")
        lifestyle_medicine.navigate()
        assert lifestyle_medicine.element_is_visible(LifestyleMedicinePage.ADDRESS_ICON), "Address icon is not visible"
        self.logger.info("--- FINISH: Lifestyle Medicine Address Icon Test ---")

    def test_schedule_now_link(self, lifestyle_medicine):        
        self.logger.info("--- START: Lifestyle Medicine Schedule Now Test ---")       
        lifestyle_medicine.sch_now_link_flow()
        self.logger.info("--- FINISH: Lifestyle Medicine Schedule Now Test ---")