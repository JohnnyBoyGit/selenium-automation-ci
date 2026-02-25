from pages.lifestyle_medicine import LifestyleMedicinePage
import pytest
from selenium.webdriver.support import expected_conditions as EC
from src.logic.lifestyle_medicine_logic import LifestyleMedicineLogic
import time

@pytest.mark.usefixtures("setup_logger")
class TestLifestyleMedicinePage:  # Lifestyle Medicine Page

    def test_lifestyle_medicine_page_title(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine Page Title Test ---")
        lifestyle_medicine.navigate()
        assert lifestyle_medicine.element_is_visible(LifestyleMedicinePage.LIFESTYLE_MEDICINE_TITLE), "Lifestyle Medicine page title is not visible"
        actual_title = lifestyle_medicine.driver.find_element(*LifestyleMedicinePage.LIFESTYLE_MEDICINE_TITLE).text
        assert LifestyleMedicineLogic.EXPECTED_TITLE in actual_title.upper()
        self.logger.info("--- FINISH: Lifestyle Medicine Page Title Test ---")
        
    def test_iv_therapy_services_link(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine IV Therapy Services Link Test ---")
        lifestyle_medicine.navigate() 
        self.logger.info("Navigated to Lifestyle Medicine page.")

        locator = LifestyleMedicinePage.IV_THERAPY_SERVICES
        assert lifestyle_medicine.element_is_visible(locator), "IV Therapy Services link is not visible on page"

        # GET EXPECTATION FROM LOGIC LAYER
        expected_url = LifestyleMedicineLogic.get_url_expectation("IV_THERAPY")

        self.logger.info(f"Clicking IV Therapy Services link with force_click: {locator}")
        lifestyle_medicine.force_click(locator)

        self.logger.info("Handling external tab if opened...")
        lifestyle_medicine.handle_external_tab()
        
        lifestyle_medicine.wait.until(
            EC.url_contains(expected_url), 
            f"Failed to land on page containing '{expected_url}'. Current: {lifestyle_medicine.driver.current_url}"
        )
        self.logger.info("Successfully verified IV Therapy redirection.")

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
        lifestyle_medicine.wait.until(EC.visibility_of_element_located(LifestyleMedicinePage.HAIR_RESTORATION_CONTENT))

        self.logger.info("Clicking Hair Restoration link again to hide content.")
        lifestyle_medicine.force_click(lifestyle_medicine.HAIR_RESTORATION)
        assert lifestyle_medicine.element_is_visible(lifestyle_medicine.HAIR_RESTORATION), "Hair Restoration link is not visible"
        self.logger.info("--- FINISH: Lifestyle Medicine Toggle Hair Restoration Content Test ---")

    def test_hair_restoration_content_link(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine Hair Restoration Content Link Test ---")
        lifestyle_medicine.navigate()
        self.logger.info("Navigated to Lifestyle Medicine page.")

        self.logger.info("Opening Hair Restoration Accordion...")
        lifestyle_medicine.force_click(LifestyleMedicinePage.HAIR_RESTORATION)

        link_locator = LifestyleMedicinePage.HAIR_RESTORATION_CONTENT_LINK
        lifestyle_medicine.wait.until(
            EC.visibility_of_element_located(link_locator),
            "Hair Restoration content link did not become visible after clicking accordion"
        )

        expected_url = LifestyleMedicineLogic.get_url_expectation("HAIR_RESTORATION")
        lifestyle_medicine.force_click(link_locator)
        
        self.logger.info("Handling external tab if opened...")
        lifestyle_medicine.handle_external_tab()
        
        lifestyle_medicine.wait.until(
            EC.url_contains(expected_url),
            f"Redirection failed. Expected slug: {expected_url}"
        )

        self.logger.info("--- FINISH: Lifestyle Medicine Hair Restoration Content Link Test ---")

    def test_hair_revitalize_link(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine Hair Revitalize Link Test ---")
        lifestyle_medicine.navigate()
        self.logger.info("Navigated to Lifestyle Medicine page.")

        locator = lifestyle_medicine.REVITALIZE
        assert lifestyle_medicine.element_is_visible(locator), "Revitalize link is not visible"
        self.logger.info("Revitalize link visibility verified.")
        self.logger.info("--- FINISH: Lifestyle Medicine Hair Revitalize Link Test ---")


    def test_toggle_revitalize_content(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine Toggle Revitalize Content Test ---")
        lifestyle_medicine.navigate()
        self.logger.info("Navigated to Lifestyle Medicine page.")
        
         # 1. Action: Click to show
        self.logger.info("Clicking Revitalize link to show content.")
        lifestyle_medicine.force_click(LifestyleMedicinePage.REVITALIZE)
        
        # 2. Senior Verification: Wait for animation/visibility
        content_locator = LifestyleMedicinePage.REVITALIZE_CONTENT
        lifestyle_medicine.wait.until(
            EC.visibility_of_element_located(content_locator),
            "Revitalize content did not become visible after click"
        )
        assert lifestyle_medicine.element_is_visible(content_locator), "Revitalize content is not visible"
        
        # 3. Action: Click to hide
        self.logger.info("Clicking Revitalize link again to hide content.")
        lifestyle_medicine.force_click(LifestyleMedicinePage.REVITALIZE)
        # (Optional: check for invisibility if the site hides the DOM element)
        self.logger.info("--- FINISH: Toggle Revitalize Content Test ---")


    def test_revitalize_content_link(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine Revitalize Content Link Test ---")
        lifestyle_medicine.navigate()
        self.logger.info("Navigated to Lifestyle Medicine page.")
        
        self.logger.info("Clicking Revitalize link to show content.")
         # Must open the accordion first
        lifestyle_medicine.force_click(LifestyleMedicinePage.REVITALIZE)

        assert lifestyle_medicine.element_is_visible(LifestyleMedicinePage.REVITALIZE_CONTENT), "Revitalize content is not visible"

        # Get expected URL from our logic layer
        expected_url = LifestyleMedicineLogic.get_url_expectation("REVITALIZE")
        link_locator = LifestyleMedicinePage.REVITALIZE_CONTENT_LINK

        # Defensive Wait + Action
        lifestyle_medicine.wait.until(EC.element_to_be_clickable(link_locator))
        self.logger.info(f"Clicking Revitalize content link: {link_locator}")
        lifestyle_medicine.force_click(link_locator)

        # Handle tab and Verify
        lifestyle_medicine.handle_external_tab() # The new robust version
        lifestyle_medicine.wait.until(
            EC.url_contains(expected_url), 
            f"Failed to reach {expected_url}. Current: {lifestyle_medicine.driver.current_url}"
        )

        self.logger.info("--- FINISH: Lifestyle Medicine Revitalize Content Link Test ---")

    def test_phone_and_address_integrity(self, lifestyle_medicine):
        """Standardized SIT check using CommonLogic."""
        self.logger.info("--- START: Lifestyle Medicine Phone and Address Integrity Test ---")
        lifestyle_medicine.navigate()
        assert lifestyle_medicine.element_is_visible(LifestyleMedicinePage.PHONE), "Phone is not visible"
        assert lifestyle_medicine.element_is_visible(LifestyleMedicinePage.ADDRESS), "Address is not visible"
        
        phone_text = lifestyle_medicine.driver.find_element(*LifestyleMedicinePage.PHONE).text
        assert LifestyleMedicineLogic.is_valid_phone_format(phone_text)
        
        address_text = lifestyle_medicine.driver.find_element(*LifestyleMedicinePage.ADDRESS).text
        assert LifestyleMedicineLogic.is_valid_address(address_text)
        self.logger.info("--- FINISH: Lifestyle Medicine Phone and Address Integrity Test ---")

    def test_validation_icons(self, lifestyle_medicine):
        self.logger.info("--- START: Lifestyle Medicine Validation Icons Test ---")
        lifestyle_medicine.navigate()
        assert lifestyle_medicine.element_is_visible(LifestyleMedicinePage.PHONE_ICON), "Phone icon is not visible"
        assert lifestyle_medicine.element_is_visible(LifestyleMedicinePage.ADDRESS_ICON), "Address icon is not visible"
        self.logger.info("--- FINISH: Lifestyle Medicine Validation Icons Test ---")

    def test_schedule_now_link(self, lifestyle_medicine):        
        self.logger.info("--- START: Lifestyle Medicine Schedule Now Test ---")       
        lifestyle_medicine.sch_now_link_flow()
        self.logger.info("--- FINISH: Lifestyle Medicine Schedule Now Test ---")