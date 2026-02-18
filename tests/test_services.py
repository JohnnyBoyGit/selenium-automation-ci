import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.services import ServicesPage

@pytest.mark.usefixtures("setup_logger")
class TestServicesPage:

    @pytest.mark.parametrize("image_key", ServicesPage.IMAGE_DATA.keys())
    def test_image_links(self, services, image_key):
        self.logger.info("--- START: Services Image Links Test ---")
        services.navigate() 
        
        locator = services.locator_by_link_slug(services.IMAGE_DATA[image_key])
        expected_url = services.IMAGE_DATA[image_key]
        
        # Scroll to the image so the browser "activates" the link
        self.logger.info(f"Scrolling to image link: {locator}")
        services.scroll_to_element(locator)

        # FIX: Remove .header. so it searches the whole page
        self.logger.info(f"Clicking image link for {image_key} with force_click: {locator}")
        services.force_click(locator)
        print(services.driver.current_url)
        self.logger.info("Handling external tab if opened...")
        services.handle_external_tab()
        
        try:
            # 2026 Tip: URL waits are more stable than raw asserts
            services.wait.until(EC.url_contains(expected_url))
        except:
            actual = services.driver.current_url
            pytest.fail(f"Link {image_key} failed. Expected slug '{expected_url}' but got '{actual}'")
        
        # Cleanup tabs
        if len(services.driver.window_handles) > 1:
            self.logger.info("Closing extra tab and switching back to original.")
            services.driver.close()
            services.driver.switch_to.window(services.driver.window_handles[0])
            self.logger.info("Switched back to original tab.")

        self.logger.info("--- FINISH: Services Image Links Test ---")

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


        
        