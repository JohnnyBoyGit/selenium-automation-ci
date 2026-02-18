import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures("setup_logger")
class TestHomePage:

    def test_home_page_components_presence(self, home):
        self.logger.info("--- START: Header/Footer Presence Check ---")
        home.navigate()
        
        # Verify Header Component
        self.logger.info("Verifying Header components...")
        assert home.header.element_is_visible(home.header.SITE_LOGO), "Header logo is not visible"
        assert home.header.element_is_visible(home.header.SERVICES_MENU_ITEM), "Navigation menu is not visible"
        
        # Verify Footer Component
        self.logger.info("Verifying Footer components...")
        assert home.footer.element_is_visible(home.footer.FOOTER_SERVICES_PAIN_MANAGEMENT), "Footer text is not visible"
        assert home.footer.element_is_visible(home.footer.FOOTER_SOCIAL_MEDIA_TWITTER), "Social media links are not visible"    
        self.logger.info("Header and Footer verification complete.")

    @pytest.mark.parametrize("button_locator", [
        "BUTTON_READ_ME",
        "BUTTON_VIEW_ALL_SERVICES"
    ])

    def test_buttons_navigation(self, home, button_locator):
        self.logger.info(f"--- START: Navigation Test for {button_locator} ---")
        home.navigate()
        # 1. Get the locator
        locator = getattr(home, button_locator)
    
        # 2. Scroll and Verify Visibility (Your current logic)
        self.logger.info(f"Scrolling to and clicking {button_locator}")
        home.scroll_to_element(locator)
        assert home.element_is_visible(locator), f"{button_locator} is not visible"

        # 3. Click the button
        self.logger.info(f"Clicking on {button_locator}")
        home.safe_click(locator)
        

        # Log current URL to trace the redirection
        current_url = home.driver.current_url.lower()
        self.logger.info(f"Redirection landed on: {current_url}")

        if button_locator == "BUTTON_READ_ME":
            assert "about" in current_url
            self.logger.info("About page URL verified successfully.")
        elif button_locator == "BUTTON_VIEW_ALL_SERVICES":
            assert "services" in current_url
            self.logger.info("Services page URL verified successfully.")

        # Go back to home for the next parameter (optional, depending on your setup)
        self.logger.info("Navigating back to Home Page...")
        home.navigate()

        self.logger.info(f"--- FINISH: Navigation Test for {button_locator} ---")
        
    
    @pytest.mark.parametrize("button_locator", [
        "BUTTON_BOOK_AN_APPOINTMENT_1",
        "BUTTON_BOOK_AN_APPOINTMENT_2",
        "BUTTON_BOOK_AN_APPOINTMENT_3",
        "BUTTON_SCHEDULE_NOW"
    ])


    def test_appointment_buttons_navigation(self, home, button_locator):
        home.navigate()
        locator = getattr(home, button_locator)
        
        # Use the force_click for the external link
        home.force_click(locator) 
        
        # Handle the tab switch
        home.handle_external_tab()
        
        assert "calipain.com" not in home.driver.current_url.lower()



# Since scope of the setup_logger is "function", it runs before each test method.  
# By adding it here, we avoid calling it before each test method manually.
@pytest.mark.usefixtures("setup_logger")                                               
class TestCarousel:

    def test_slide_footer_rating(self, home):
        self.logger.info("--- START: Carousel Footer Rating Verification ---")
        home.navigate()
         
         # 1. Trigger Hydration
        self.logger.info("Triggering Carousel Hydration (Scroll/Resize/Hover)")
        home.driver.execute_script("window.scrollTo(0, 5000);")
        home.driver.execute_script("window.dispatchEvent(new Event('resize'));")
        ActionChains(home.driver).move_by_offset(10, 10).perform()

        # 2. WAIT for the footer area to exist first
        # This ensures the JavaScript has actually rendered the footer
        self.logger.info("Waiting for Trustindex footer to render...")
        home.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "ti-footer")),
            "The Trustindex footer never loaded."
        )

        # 3. Assertions (Now they will find the elements)
        self.logger.info("Verifying footer rating elements...")
        assert home.element_is_visible(home.CAROUSEL_RATING), "Rating is not visible"
        assert home.element_is_visible(home.CAROUSEL_RATING_STARS), "Rating stars are not visible"
        assert home.element_is_visible(home.CAROUSEL_RATING_TEXT), "Rating text is not visible"
        assert home.element_is_visible(home.CAROUSEL_RATING_LOGO), "Rating logo is not visible"
        rating = home.driver.find_element(*home.CAROUSEL_RATING).text
        self.logger.info(f"Captured Footer Rating: {rating}")
        assert "EXCELLENT" in rating.text

        self.logger.info("--- FINISH: Carousel Footer Rating Verification ---")

    def test_next_navigation(self, home):
        self.logger.info("--- START: Carousel Next Button Navigation Test ---")
        home.navigate()

        # 1. Trigger Hydration
        self.logger.info("Triggering Carousel Hydration (Scroll/Resize/Hover)")
        home.driver.execute_script("window.scrollTo(0, 5000);")
        home.driver.execute_script("window.dispatchEvent(new Event('resize'));")
        ActionChains(home.driver).move_by_offset(10, 10).perform()

        # 2. Get Initial Name
        self.logger.info("Waiting for active slide to render...")
        home.wait.until(lambda d: home.get_active_slide() is not None)
        initial_name = home.get_active_slide().find_element(By.CLASS_NAME, "ti-name").text

        # 3. Click Next via JS
        next_btn = home.driver.find_element(*home.NEXT_BUTTON)("Clicking Next button via JS...")
        self.logger.info("Clicking Next button to move forward...")
        home.driver.execute_script("arguments[0].click();", next_btn)

        # 4. Wait for the slide content to change("Waiting for slide content to change...")
        home.wait.until(
            lambda d: home.get_active_slide().find_element(By.CLASS_NAME, "ti-name").text != initial_name
        )

        # 5. Assertion
        new_name = home.get_active_slide().find_element(By.CLASS_NAME, "ti-name").text
        assert new_name != initial_name, f"Next failed: slide name is still {initial_name}"
        self.logger.info(f"Navigation successful. New slide: {new_name}")

        self.logger.info("--- FINISH: End of Carousel Next Button Navigation Test ---")


    def test_prev_navigation(self, home):
        self.logger.info("--- START: Carousel Previous Button Navigation Test ---")
        home.navigate()
        
        # 1. Trigger Hydration
        self.logger.info("Triggering Carousel Hydration (Scroll/Resize/Hover)")
        home.driver.execute_script("window.scrollTo(0, 5000);")
        home.driver.execute_script("window.dispatchEvent(new Event('resize'));")
        
        # Fake human mouse movement to wake up the script
        self.logger.info("Simulating human mouse movement...")
        actions = ActionChains(home.driver)
        actions.move_by_offset(100, 100).pause(0.5).perform()

        # 2. WAIT for slides to populate (Using your existing home.wait)
        # We wait until the list of elements is no longer empty
        self.logger.info("Waiting for Trustindex slides to populate...")
        home.wait.until(
            lambda d: len(d.find_elements(*home.ALL_SLIDES)) > 0,
            "Timed out waiting for Trustindex slides to hydrate."
        )
        self.logger.info("Slides populated successfully.")

        # 3. Get Next Button and move forward
        self.logger.info("Clicking Next button to move forward...")
        next_btn = home.wait.until(EC.presence_of_element_located(home.NEXT_BUTTON))
        home.driver.execute_script("arguments[0].click();", next_btn)
        
        # 4. Capture the name of the first visible slide
        self.logger.info("Capturing the name of the currently active slide...")
        home.wait.until(lambda d: home.get_active_slide() is not None)
        initial_name = home.get_active_slide().find_element(By.CLASS_NAME, "ti-name").text

        # 5. Get Prev Button and move back        
        prev_btn = home.wait.until(EC.presence_of_element_located(home.PREV_BUTTON))
        self.logger.info("Clicking Previous button to return to initial slide...")
        home.driver.execute_script("arguments[0].click();", prev_btn)

        # 6. Wait for the text to change back
        home.wait.until(
            lambda d: home.get_active_slide().find_element(By.CLASS_NAME, "ti-name").text != initial_name
        )
        
        # 7. Final Verification
        new_name = home.get_active_slide().find_element(By.CLASS_NAME, "ti-name").text
        assert new_name != initial_name, f"Previous navigation failed: slide name is still {initial_name}"
        self.logger.info(f"Navigation successful. New slide: {new_name}")

        self.logger.info("--- FINISH: End of Carousel Previous Button Navigation Test ---")


    # Parametrize allows us to run this test twice: once for 'Next' and once for 'Prev'
    @pytest.mark.parametrize("direction", ["next", "prev"])
    def test_carousel_navigation_both_ways(self, home, direction):
        self.logger.info(f"===== START: test_carousel_navigation [{direction}] =====")
        home.navigate()

        self.logger.info("Hydrating carousel and capturing initial slide...")
        home.driver.execute_script("window.scrollTo(0, 5000);")
        home.driver.execute_script("window.dispatchEvent(new Event('resize'));")
        ActionChains(home.driver).move_by_offset(100, 100).perform() 

        # 2. Capture Initial State (The first visible slide)
        home.wait.until(lambda d: home.get_active_slide() is not None)
        initial_name = home.get_active_slide().find_element(By.CLASS_NAME, "ti-name").text
        self.logger.info(f"Initial Slide: {initial_name}")
        
        # 3. Determine which button to click
        btn_locator = home.NEXT_BUTTON if direction == "next" else home.PREV_BUTTON
        btn = home.driver.find_element(*btn_locator)
        
        # 4. Click and Wait for Change
        self.logger.info(f"Clicking {direction} button.")
        home.driver.execute_script("arguments[0].click();", btn)
        
        # 5. Wait until the first visible slide name is different from the initial one
        try:
            home.wait.until(
                lambda d: home.get_active_slide().find_element(By.CLASS_NAME, "ti-name").text != initial_name,
                message=f"Carousel failed to move in the {direction} direction."
            )
            
            # 6. Final Assertion
            new_name = home.get_active_slide().find_element(By.CLASS_NAME, "ti-name").text
            assert new_name != initial_name
            self.logger.info(f"Navigation successful. New slide: {new_name}")
        except Exception as e:
            self.logger.error(f"Carousel failed to move {direction}. Current slide is still {initial_name}")
            raise e
        
        self.logger.info("===== FINISH: test_carousel_navigation =====")


    def test_slide_expansion_and_collapse(self, home):
        self.logger.info("--- START: Carousel Slide Expansion and Collapse Test ---")
        home.navigate()
        
        # 1. TRIGGER HYDRATION
        self.logger.info("Triggering Carousel Hydration (Scroll/Resize/Hover)")
        home.driver.execute_script("window.scrollTo(0, 5000);")
        home.driver.set_window_size(1920, 1080)

        self.logger.info("Simulating human mouse movement...")
        actions = ActionChains(home.driver)
        actions.move_by_offset(100, 100).pause(0.5).perform()

        self.logger.info("Dispatching resize and scroll events...")
        home.driver.execute_script("window.dispatchEvent(new Event('resize'));")
        home.driver.execute_script("window.dispatchEvent(new Event('scroll'));")

        # 2. WAIT FOR SLIDES
        self.logger.info("Waiting for Trustindex slides to populate...")
        slides = home.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ti-review-item"))
        )

        for slide in slides:
            # Only test slides that are visible and have a 'Read more' button
            self.logger.info("Checking slide for expansion capability...")
            if slide.is_displayed() and slide.get_attribute("data-empty") == "0":
                home.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", slide)
                
                btn = slide.find_element(By.CSS_SELECTOR, ".ti-read-more-active")
                text_container = slide.find_element(By.CSS_SELECTOR, ".ti-review-content")

                # --- CAPTURE INITIAL HEIGHT ---
                initial_height = text_container.size['height']

                # --- EXPAND ---
                self.logger.info("Clicking 'Read more' to expand the slide...")
                home.driver.execute_script("arguments[0].click();", btn)
                home.wait.until(lambda d: btn.get_attribute("aria-label") == "Hide")
                self.logger.info("Button's caption changed to 'Hide'...")                

                # --- WAIT FOR ANIMATION TO FINISH ---
                # This waits until the height is actually greater than the initial height
                self.logger.info("Waiting for slide to expand...")
                home.wait.until(lambda d: text_container.size['height'] > initial_height)
                
                # --- ASSERT HEIGHT INCREASED ---
                expanded_height = text_container.size['height']
                assert expanded_height > initial_height, f"Slide height did not increase. Initial: {initial_height}, Expanded: {expanded_height}"
                self.logger.info(f"Expansion successful. Initial Height: {initial_height}, Expanded Height: {expanded_height}")

                            # --- COLLAPSE ---
                self.logger.info("Clicking 'Hide' to collapse the slide...")
                home.driver.execute_script("arguments[0].click();", btn)
                
                # 1. Wait for the label to change back to "Read more"
                home.wait.until(lambda d: btn.get_attribute("aria-label") == "Read more")
                self.logger.info("Button's caption changed back to 'Read more'...")
                
                # 2. CRITICAL: Wait for the height to shrink back to the original size
                # This handles the 0.3s - 0.5s CSS animation
                home.wait.until(lambda d: text_container.size['height'] == initial_height)
                self.logger.info("Slide collapsed back to initial height.")

                # --- ASSERT HEIGHT RETURNED TO NORMAL ---
                final_height = text_container.size['height']
                assert final_height == initial_height, f"Collapse failed! Final: {final_height}, Expected: {initial_height}"
                self.logger.info(f"Collapse successful. Final Height: {final_height}")
                self.logger.info("--- FINISH: Carousel Slide Expansion and Collapse Test ---")

