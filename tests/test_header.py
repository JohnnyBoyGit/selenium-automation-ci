import pytest
from selenium.webdriver.support import expected_conditions as EC
from src.logic.header_logic import HeaderLogic

@pytest.mark.usefixtures("setup_logger")
class TestHeader:   # Simple class, no inheritance needed.


    @pytest.mark.parametrize("button_name", HeaderLogic.NAV_MAP.keys())
    def test_link_navigation(self, home, button_name):
        """Verifies that each link redirects to the correct destination."""
        home.navigate()
        
        expected_url = HeaderLogic.get_expected_url(button_name)
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
        home.wait.until(
            EC.url_contains(expected_url), 
            f"Header link {button_name} failed. URL: {home.driver.current_url}"
        )

