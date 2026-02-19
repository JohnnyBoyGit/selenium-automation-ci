import pytest
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup_logger")
class TestHeader:   # Simple class, no inheritance needed.

    # Define your test data: (Button Name, Partial Expected URL)
    HEADER_DATA = [
        ("SITE_LOGO", "calipain.com"),
        ("HOME_MENU_ITEM", "calipain.com"),
        ("ABOUT_MENU_ITEM", "/about"),
        ("SERVICES_MENU_ITEM", "/services"),
        ("CONTACT_MENU_ITEM", "/contact"),
        ("SERVICES_SUBMENU_PAIN_MANAGEMENT", "pain-management"),
        ("SERVICES_SUBMENU_ELECTRODIAGNOSTICS", "electrodiagnostic"),
        ("SERVICES_SUBMENU_INDEPENDENT_MEDICAL_EXAMS", "independent-medical-exams"),
        ("SERVICES_SUBMENU_INFUSION_THERAPY", "infusion-therapy"),
        ("SERVICES_SUBMENU_PLATELET_RICH_PLASMA_PRP", "platelet-rich-plasma-prp"),
        ("SERVICES_SUBMENU_LIFESTYLE_MEDICINE", "lifestyle-medicine")  
]

    @pytest.mark.parametrize("button_name, expected_url", HEADER_DATA)
    def test_link_navigation(self, home, button_name, expected_url):
        """Verifies that each link redirects to the correct destination."""
        home.navigate()
        
        # 1. Get the locator from the HomePage class dynamically
        locator = getattr(home.header, button_name)

        # 2. Click the element
        # If it's a submenu item, we might need to hover first
        if "SUBMENU" in button_name:
            self.logger.info(f"Hovering over Services menu...")
            home.header.hover(home.header.SERVICES_MENU_ITEM)
            # Ensure the submenu is visible before clicking
            home.wait.until(EC.visibility_of_element_located(locator))

        home.header.quick_click(locator)
        
        # 3. Handle the new tab if it opens
        home.handle_external_tab()
        
        # 4. Assert the result
        try:
            home.wait.until(EC.url_contains(expected_url))
        except:
            pytest.fail(f"Link {button_name} failed. Expected '{expected_url}' but got '{home.driver.current_url}'")
        
        # 5. Optional Cleanup: If it was a new tab, close it
        if len(home.driver.window_handles) > 1:
            home.driver.close()
            home.driver.switch_to.window(home.driver.window_handles[0])

