import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.services import ServicesPage
from src.logic.services_logic import ServicesLogic

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

    @pytest.mark.parametrize("service_key", ServicesPage.APPOINTMENT_DATA.keys())   # use the keys from APPOINTMENT_DATA dictionary
    def test_appointment_links(self, services, service_key):
        self.logger.info("--- START: Services Appointment Links Test ---") 
        # Use the services_page's own navigation
        services.navigate() 
        self.logger.info("Navigated to Services page.")
        
        # Call the dynamic locator method instead of getattr
        locator = services.get_appointment_locator(service_key)
        
         # Click the link
        self.logger.info(f"Clicking appointment link for {service_key} with safe_click: {locator}")
        services.safe_click(locator)
        self.logger.info("Handling external tab if opened...")
        services.handle_external_tab()
         
         # Verify navigation to the booking page
        assert "booking" in services.driver.current_url.lower()
        self.logger.info("--- FINISH: Services Appointment Links Test ---")


        
        