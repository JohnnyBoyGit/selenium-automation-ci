import pytest
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup_logger")
class TestFooter:   # Simple class, no inheritance needed.
    
    FOOTER_DATA = [
        ("FOOTER_SOCIAL_MEDIA_FACEBOOK", "facebook.com"),
        ("FOOTER_SOCIAL_MEDIA_INSTAGRAM", "instagram.com"),
        ("FOOTER_SOCIAL_MEDIA_GOOGLE", "Joseph+Hadi"),
        ("FOOTER_SOCIAL_MEDIA_TWITTER", "x.com/joehadimd"),
        ("FOOTER_QUICK_LINKS_ABOUT_US", "about"),
        ("FOOTER_QUICK_LINKS_SERVICES", "services"),
        ("FOOTER_QUICK_LINKS_APPOINTMENTS", "booking"),
        ("FOOTER_QUICK_LINKS_CONTACT_US", "contact"),
        ("FOOTER_SERVICES_PAIN_MANAGEMENT", "pain-management"),
        ("FOOTER_SERVICES_ELECTRODIAGNOSTICS", "electrodiagnostic"),
        ("FOOTER_SERVICES_IME", "independent-medical-exams"),
        ("FOOTER_SERVICES_PLATELET_RICH_PLASMA", "platelet-rich-plasma-prp"),
        ("FOOTER_SERVICES_INFUSION_THERAPY", "infusion-therapy"),
        ("FOOTER_SERVICES_LIFESTYLE_MEDICINE", "lifestyle-medicine"),
        ("FOOTER_PRIVACY_POLICY", "privacy-policy"),
        ("FOOTER_TERMS_AND_CONDITIONS", "terms")      
]

    @pytest.mark.parametrize("button_name, expected_url", FOOTER_DATA)
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
        try:
            home.wait.until(EC.url_contains(expected_url))
        except:
            pytest.fail(f"Link {button_name} failed. Expected '{expected_url}' but got '{home.driver.current_url}'")
        
        # 5. Optional Cleanup: If it was a new tab, close it
        if len(home.driver.window_handles) > 1:
            home.driver.close()
            home.driver.switch_to.window(home.driver.window_handles[0])