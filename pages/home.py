from selenium.webdriver.common.by import By
from pages.base import BasePage
from src.logic.home_logic import HomeLogic

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)    # This gives you self.header and self.footer automatically

     # Locators stored as tuples
    # No space between the class and the 'a'
    BUTTON_BOOK_AN_APPOINTMENT_1 = (By.CSS_SELECTOR, "a.ast-custom-button-link[href*='booking']")
    BUTTON_BOOK_AN_APPOINTMENT_2 = (By.CSS_SELECTOR, "[data-id='c8c2752'] a[href*='booking']")
    BUTTON_BOOK_AN_APPOINTMENT_3 = (By.CSS_SELECTOR, "[data-id='560d836'] a[href*='booking']")
    BUTTON_BOOK_AN_APPOINTMENT_4 = (By.CSS_SELECTOR, "[data-id='b3ab0db'] a[href*='booking']")
    BUTTON_SCHEDULE_NOW = (By.CSS_SELECTOR, "[data-id='abbbe43'] a[href*='booking']")
    BUTTON_READ_ME = (By.CSS_SELECTOR, "[data-id='3bd16c5'] a[href*='/about']")
    BUTTON_VIEW_ALL_SERVICES = (By.CSS_SELECTOR, "[data-id='6ac4a4b'] a[href*='/services']")

    CAROUSEL_RATING = (By.CSS_SELECTOR, ".ti-rating.ti-rating-large")
    CAROUSEL_RATING_STARS = (By.CSS_SELECTOR, ".ti-stars.star-lg")
    CAROUSEL_RATING_TEXT = (By.CLASS_NAME, "nowrap")
    CAROUSEL_RATING_LOGO = (By.CLASS_NAME, "ti-logo-fb")

    NEXT_BUTTON = (By.CLASS_NAME, "ti-next")
    PREV_BUTTON = (By.CLASS_NAME, "ti-prev")
    ALL_SLIDES = (By.CSS_SELECTOR, ".ti-review-item")
    READ_MORE_BTN = (By.CSS_SELECTOR, ".ti-read-more-active")

   
    def navigate(self):
        """Uses the Logic Layer to navigate home."""
        self.open_url(HomeLogic.EXPECTED_PATH)  



    def get_active_slide(self):
        slides = self.driver.find_elements(*self.ALL_SLIDES)
        for index, slide in enumerate(slides):
            if slide.is_displayed():
                try:
                    # Use the reviewer name as a "Unique ID" for the log
                    name = slide.find_element(By.CLASS_NAME, "ti-name").text
                    # self.logger.debug(f"Active slide detected at index {index}: '{name}'")
                    self.logger.debug(f"[{self.__class__.__name__}] Found active slide.")
                except:
                    self.logger.debug(f"Active slide detected at index {index} (Name not found)")
                return slide
        self.logger.debug("No active slide detected!")   
        return None
    
        


    



    