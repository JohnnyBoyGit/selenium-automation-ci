import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from src.logic.home_logic import HomeLogic

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

        locator = getattr(home, button_locator)
        home.scroll_to_element(locator)
        assert home.element_is_visible(locator), f"{button_locator} is not visible"

        # Click and Handle Tab
        home.safe_click(locator)
        home.handle_external_tab()
        
        # SENIOR MOVE: Use Logic Layer instead of hardcoded 'if/elif' blocks
        expected_slug = HomeLogic.get_url_expectation(button_locator)
        home.wait.until(
            EC.url_contains(expected_slug), 
            f"Failed to reach {expected_slug}. Current URL: {home.driver.current_url}"
        )

        self.logger.info(f"--- FINISH: Navigation Test for {button_locator} ---")
        
    
    @pytest.mark.parametrize("button_locator", [
        "BUTTON_BOOK_AN_APPOINTMENT_1",
        "BUTTON_BOOK_AN_APPOINTMENT_2",
        "BUTTON_BOOK_AN_APPOINTMENT_3",
        "BUTTON_BOOK_AN_APPOINTMENT_4",
        "BUTTON_SCHEDULE_NOW"
    ])
    def test_appointment_buttons_navigation(self, home, button_locator):
        self.logger.info(f"--- START: Appointment Button Navigation Test for {button_locator} ---")
        home.navigate()
        locator = getattr(home, button_locator)
        
        home.force_click(locator) 
        home.handle_external_tab()
        
        # Strong assertion using Logic Layer
        expected = HomeLogic.get_url_expectation(button_locator)
        home.wait.until(EC.url_contains(expected), f"Booking page not reached via {button_locator}")

        self.logger.info(f"--- FINISH: Appointment Button Navigation Test for {button_locator} ---")


# Since scope of the setup_logger is "function", it runs before each test method.  
# By adding it here, we avoid calling it before each test method manually.
@pytest.mark.usefixtures("setup_logger")                                               
class TestCarousel:

    def test_slide_footer_rating(self, home):
        self.logger.info("--- START: Carousel Footer Rating Verification ---")
        home.navigate()
        
        # 1. Trigger Hydration
        self.logger.info("Triggering Carousel Hydration...")
        try:
            widget = home.driver.find_element(By.CLASS_NAME, "ti-widget")
            home.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", widget)
            ActionChains(home.driver).move_to_element(widget).pause(0.5).perform()
        except:
            home.driver.execute_script("window.scrollTo(0, 5000);")
            # Fallback: Move to a safe offset if the specific class isn't found
            ActionChains(home.driver).move_by_offset(10, 10).perform()

        # 2. WAIT for the footer area to exist
        self.logger.info("Waiting for Trustindex footer to render...")
        home.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "ti-footer")),
            "The Trustindex footer never loaded."
        )

        # 3. Assertions
        self.logger.info("Verifying footer rating elements...")
        assert home.element_is_visible(home.CAROUSEL_RATING), "Rating is not visible"
        assert home.element_is_visible(home.CAROUSEL_RATING_STARS), "Rating stars are not visible"
        assert home.element_is_visible(home.CAROUSEL_RATING_TEXT), "Rating text is not visible"
        assert home.element_is_visible(home.CAROUSEL_RATING_LOGO), "Rating logo is not visible"
        
        # 4. Fixed logic: rating is a string, check membership directly
        rating_text = home.driver.find_element(*home.CAROUSEL_RATING).text
        assert HomeLogic.is_rating_valid(rating_text), f"Unexpected rating: {rating_text}"
        self.logger.info(f"Captured and verified Footer Rating: {rating_text}")

        self.logger.info("--- FINISH: Carousel Footer Rating Verification ---")


    def test_next_navigation(self, home):
        self.logger.info("--- START: Carousel Next Button Navigation Test ---")
        home.navigate()

        # 1. Trigger Hydration & Scroll
        self.logger.info("Triggering Carousel Hydration via Scroll & Hover...")
        try:
            widget = home.driver.find_element(By.CLASS_NAME, "ti-widget")
            home.driver.execute_script("arguments.scrollIntoView({block: 'center'});", widget)
            home.driver.execute_script("window.dispatchEvent(new Event('scroll'));")
            # Your added line: High-accuracy hover
            ActionChains(home.driver).move_to_element(widget).pause(0.5).perform()
            self.logger.info("Targeted hover successful.")
        except Exception as e:
            self.logger.warning(f"Could not find widget, falling back: {e}")
            home.driver.execute_script("window.scrollTo(0, 5000);")
            # Your added line: General activity hover
            ActionChains(home.driver).move_by_offset(10, 10).perform()

        # 2. Wait for the ACTIVE slide content to be visible
        name_locator = (By.CLASS_NAME, "ti-name")
        self.logger.info("Waiting for active slide content...")
        
        # We wait specifically for the text element inside the active slide
        home.wait.until(
            EC.visibility_of_element_located(name_locator),
            "Review content (ti-name) did not become visible."
        )
        
        initial_name = home.get_active_slide().find_element(*name_locator).text
        self.logger.info(f"Initial slide detected: {initial_name}")

        # 3. Click Next via JS (Using the button locator from your 'home' object)
        self.logger.info("Clicking Next button...")
        next_btn = home.driver.find_element(*home.NEXT_BUTTON)
        home.driver.execute_script("arguments[0].click();", next_btn)

        # 4. Wait for the slide content to change
        # This is the most important part for stability
        home.wait.until(
            lambda d: home.get_active_slide().find_element(*name_locator).text != initial_name,
            message=f"Slide text stayed as '{initial_name}' after clicking next."
        )

        # 5. Final Assertion
        new_name = home.get_active_slide().find_element(*name_locator).text
        assert new_name != initial_name, "Navigation failed: New name matches initial name."
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

