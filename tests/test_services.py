import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.services import ServicesPage
from src.logic.services_logic import ServicesLogic
from src.logic.common_logic import CommonLogic

@pytest.mark.usefixtures("setup_logger")
class TestServicesPage:

    @pytest.mark.parametrize("image_key", ServicesLogic.get_all_image_keys())
    def test_image_links(self, services, image_key):
        self.logger.info("--- START: Services Image Links Test for {image_key}---")
        services.navigate() 
        
        # Logic Layer provides the expected slug
        expected_slug = ServicesLogic.get_slug(image_key)
        locator = services.locator_by_link_slug(expected_slug)
        
        # Scroll to the image so the browser "activates" the link
        self.logger.info(f"Scrolling to image link: {locator}")
        services.scroll_to_element(locator)

        # FIX: Remove .header. so it searches the whole page
        self.logger.info(f"Clicking image link for {image_key} with force_click: {locator}")
        services.force_click(locator)

        self.logger.info("Handling external tab if opened...")
        services.handle_external_tab()
        
        # One line that waits AND asserts. 
        # If it fails, Selenium throws a 'TimeoutException' which Pytest marks as a failure automatically.
        services.wait.until(EC.url_contains(expected_slug), f"Expected slug '{expected_slug}' not found in {services.driver.current_url}")
        
        self.logger.info("--- FINISH: Services Image Links Test for {image_key}---")

    @pytest.mark.parametrize("service_key", ServicesPage.APPOINTMENT_DATA.keys())
    def test_service_appointment_links(self, services, service_key):
        self.logger.info(f"--- START: Services Appointment Link Test for {service_key} ---") 
        
        # 1. Get the dynamic locator (Method you already have in ServicesPage)
        locator = services.get_appointment_locator(service_key)
        
        # 2. Define the expectation (usually "booking" for all services)
        expected = "booking" 
        
        # 3. Use the UNIFIED Engine
        # Note: Services usually need 'safe' click and 'scroll' to be True
        CommonLogic.verify_link_flow(
            page=services, 
            locator=locator, 
            expected_slug=expected, 
            click_type="safe",
            scroll=True
        )

        self.logger.info(f"--- FINISH: Services Appointment Link Test for {service_key} ---")


        
        