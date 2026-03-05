import logging
from time import time
from time import sleep  # Import the specific function
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.custom_logger import LogGen
from utils.read_config import ReadConfig

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.base_url = ReadConfig.get_application_url()
        
        # Initialize logger
        base_logger = LogGen.loggen()
        self.logger = logging.LoggerAdapter(base_logger, {"page_name": self.__class__.__name__})

    @property
    def header(self):
        from pages.components.header_component import HeaderComponent
        return HeaderComponent(self.driver)

    @property
    def footer(self):
        from pages.components.footer_component import FooterComponent
        return FooterComponent(self.driver)

    def open_url(self, path=""):
        base_url = "https://calipain.com/"
        full_url = f"{base_url}{path}"
        self.logger.info(f"Opening URL: {full_url}")
        self.driver.get(full_url)

    def find_element(self, locator):
        self.logger.info(f"Finding element: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))


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

    def quick_click(self, locator):
        """Wait and click without scrolling—best for Header/Nav menus."""
        self.logger.info(f"Attempting quick_click on: {locator}")
        # 1. Wait for visibility/clickability
        element = self.wait.until(EC.element_to_be_clickable(locator))
        
        try:
            # 2. Native click first
            element.click()
            self.logger.info("Quick native click successful.")
        except Exception:
            # 3. JS Fallback if something (like a transparent overlay) is in the way
            self.logger.warning("Quick click failed, using JS fallback.")
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


    def handle_external_tab(self, timeout=10):
        """
        Senior approach: Wait for the tab handle to exist before switching.
        This eliminates race conditions.
        """
        self.logger.info(f"Waiting up to {timeout}s for a new tab to appear...")
        
        try:
            # 1. Wait until the count of windows is at least 2
            WebDriverWait(self.driver, timeout).until(
                lambda d: len(d.window_handles) > 1
            )
            
            # 2. Switch to the last handle (the newest tab)
            new_handle = self.driver.window_handles[-1]
            self.driver.switch_to.window(new_handle)
            
            self.logger.info(f"Switched to new tab: {self.driver.current_url}")
            return True
        
        except Exception:
            self.logger.error("TIMEOUT: New tab did not appear within the allotted time.")
            return False


    def hover(self, locator):
        self.logger.info(f"Hovering over: {locator}")
        from selenium.webdriver.common.action_chains import ActionChains
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()


    