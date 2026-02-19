import logging
from time import time
from time import sleep  # Import the specific function
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.custom_logger import LogGen


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.base_url = "https://calipain.com/"
        
        current_class = self.__class__.__name__

        # 1. Get the base logger
        base_logger = LogGen.loggen()
        
        # 2. Wrap it so it automatically injects the class name
        self.logger = logging.LoggerAdapter(base_logger, {"page_name": self.__class__.__name__})
        
        if current_class not in ["HeaderComponent", "FooterComponent"]:
            from pages.components.header_component import HeaderComponent
            from pages.components.footer_component import FooterComponent
            
            # Use the local imports to set the attributes
            self.header = HeaderComponent(driver)
            self.footer = FooterComponent(driver)

    def open_url(self, path=""):
        base_url = "https://calipain.com/"
        full_url = f"{base_url}{path}"
        self.logger.info(f"Opening URL: {full_url}")
        self.driver.get(full_url)

    def find_element(self, locator):
        self.logger.info(f"Finding element: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    from time import sleep # Direct import to avoid 'builtin_function_or_method' error

    def safe_click(self, locator):
        self.logger.info(f"Attempting safe_click on: {locator}")
        
        # 1. Force a scroll to the bottom to 'wake up' the footer
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1) # Wait for footer animation/render to finish
        
        # 2. Wait for the element specifically
        element = self.wait.until(EC.element_to_be_clickable(locator))
        
        # 3. Ensure it's centered in the viewport
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        sleep(0.5)

        try:
            element.click()
            self.logger.info("Native click successful.")
        except Exception:
            self.logger.warning("Native click blocked; using JS fallback.")
            # Ensure 'element' is passed correctly into the JS script
            self.driver.execute_script("arguments[0].click();", element)


    def force_click(self, locator):
        self.logger.info(f"Executing force_click (JS) on: {locator}")
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def click_with_actions(self, locator):
        self.logger.info(f"Executing ActionChains click on: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        ActionChains(self.driver).move_to_element(element).click().perform()

    def element_is_visible(self, locator):
        self.logger.info(f"Checking visibility of: {locator}")
        try:
            is_visible = self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
            self.logger.info(f"Element visible: {is_visible}")
            return is_visible
        except:
            self.logger.warning(f"Element {locator} not visible within timeout.")
            return False
            
    def scroll_to_element(self, locator):
        self.logger.info(f"Scrolling to element: {locator}")
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", 
            element
        )
        self.wait.until(EC.visibility_of_element_located(locator))

    def handle_external_tab(self):
        self.logger.info("Checking for new browser tabs/windows.")
        if len(self.driver.window_handles) > 1: # Checks if the number of currently opened tabs is more than 1
            self.driver.switch_to.window(self.driver.window_handles[-1]) # Switches to the last opened tab
            self.logger.info(f"Switched to new tab. Current URL: {self.driver.current_url}")
            return True
        self.logger.warning("No external tab found to switch to.")
        return False

    def hover(self, locator):
        self.logger.info(f"Hovering over: {locator}")
        from selenium.webdriver.common.action_chains import ActionChains
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()


    def sch_now_link_flow(self, expected_slug="booking"):
        """
        Coordinates the booking link verification.
        No need to pass 'pagefixture' because 'self' is the page object.
        """
        # Add this to confirm the page object is created correctly
        self.logger.info(f"Starting 'Schedule Now' flow for: {self.__class__.__name__}")
        
        # 1. Navigate to the page
        # This calls the navigate() method of whichever page is currently running
        self.navigate() 
        
        # 2. Get the locator from the specific Page Object (self)
        # Note: This assumes every page using this has a SCH_NOW_BUTTON defined
        locator = self.SCH_NOW_BUTTON
        
        self.logger.info(f"Targeting booking link with locator: {locator}")
        self.scroll_to_element(locator)

        # 3. Click and handle tabs
        #self.force_click(locator)
        self.safe_click(locator)
        self.handle_external_tab()

        # 4. Wait for URL change
        try:
            self.logger.info(f"Verifying URL contains slug: '{expected_slug}'")
            self.wait.until(EC.url_contains(expected_slug))
            self.logger.info("Verification successful.")
        except Exception as e:
            # Use actual_url variable to keep the log clean
            actual_url = self.driver.current_url
            self.logger.error(f"Mismatch! Search Slug: '{expected_slug}' | Actual URL: {actual_url}")
            raise e

