import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.about import AboutPage

@pytest.mark.usefixtures("setup_logger")
class TestAboutPage:
    def test_about_us_title(self, about):
        self.logger.info("--- START: About Us Title Test ---")
        about.navigate()
        assert about.element_is_visible(AboutPage.ABOUT_US_TITLE), "About Us title is not visible"
        self.logger.info("--- FINISH: About Us Title Test ---")

    def test_phone(self, about):
        self.logger.info("--- START: About Us Phone Test ---")
        about.navigate()
        assert about.element_is_visible(AboutPage.PHONE), "Phone is not visible"
        self.logger.info("--- FINISH: About Us Phone Test ---")

    def test_address(self, about):
        self.logger.info("--- START: About Us Address Test ---")
        about.navigate()
        assert about.element_is_visible(AboutPage.ADDRESS), "Address is not visible"
        self.logger.info("--- FINISH: About Us Address Test ---")

    def test_phone_icon(self, about):
        self.logger.info("--- START: About Us Phone Icon Test ---")
        about.navigate()
        assert about.element_is_visible(AboutPage.PHONE_ICON), "Phone icon is not visible"
        self.logger.info("--- FINISH: About Us Phone Icon Test ---")
    def test_address_icon(self, about):
        self.logger.info("--- START: About Us Address Icon Test ---")
        about.navigate()
        assert about.element_is_visible(AboutPage.ADDRESS_ICON), "Address icon is not visible"
        self.logger.info("--- FINISH: About Us Address Icon Test ---")


    def test_appointment_link(self, about):
        # Use the about_page's own navigation
        self.logger.info("--- START: About Us Appointment Link Test ---")
        about.navigate() 
        self.logger.info("Navigated to About Us page.")

        locator = AboutPage.BUTTON_BOOK_AN_APPOINTMENT

        expected_url = "booking"
        
        # Scroll to the image so the browser "activates" the link
        self.logger.info(f"Scrolling to appointment link: {locator}")
        about.scroll_to_element(locator)

        # FIX: Remove .header. so it searches the whole page
        self.logger.info(f"Clicking appointment link with force_click: {locator}")
        about.force_click(locator)

        self.logger.info("Handling external tab if opened...")
        about.handle_external_tab()
        
        try:
            # 2026 Tip: URL waits are more stable than raw asserts
            about.wait.until(EC.url_contains(expected_url))
        except:
            actual = about.driver.current_url
            pytest.fail(f"Link {locator} failed. Expected slug '{expected_url}' but got '{actual}'")
        
        # Cleanup tabs
        if len(about.driver.window_handles) > 1:
            self.logger.info("Closing external tab and switching back.")
            about.driver.close()            
            about.driver.switch_to.window(about.driver.window_handles[0])
            self.logger.info("Switched back to original tab.")

        self.logger.info("--- FINISH: About Us Appointment Link Test ---")


    def test_schedule_now_link(self, about):        
        self.logger.info("--- START: About Us Schedule Now Test ---")       
        about.sch_now_link_flow()
        self.logger.info("--- FINISH: About Us Schedule Now Test ---")

    