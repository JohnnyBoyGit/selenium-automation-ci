import pytest
from selenium.webdriver.support import expected_conditions as EC
from src.logic.footer_logic import FooterLogic


@pytest.mark.usefixtures("setup_logger")
class TestFooter:   # Simple class, no inheritance needed.
    
    # Senior Move: Combine valid and broken links with marks dynamically
    FOOTER_PARAMS = [
        (k, v) for k, v in FooterLogic.NAV_MAP.items()
    ] + [
        pytest.param(k, v, marks=pytest.mark.xfail(reason="Site 404")) 
        for k, v in FooterLogic.BROKEN_LINKS.items()
    ]

    @pytest.mark.parametrize("button_name, expected_url", FOOTER_PARAMS)
    def test_link_navigation(self, home, button_name, expected_url):
        """Verifies that each link redirects to the correct destination."""
        home.navigate()
        
        # 1. Get the locator from the HomePage class dynamically
        locator = getattr(home.footer, button_name)

        # 2. Click the element
        home.footer.safe_click(locator)
        
        # 3. Handle the new tab if it opens
        home.handle_external_tab()
        
        # 4. Assert the result
        home.wait.until(
            EC.url_contains(expected_url), 
            f"Footer link {button_name} failed. URL: {home.driver.current_url}"
        )