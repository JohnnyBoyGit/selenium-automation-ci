from selenium.webdriver.common.by import By
from pages.base import BasePage

class FooterComponent(BasePage):

    # Locators stored as tuples
    FOOTER_SOCIAL_MEDIA_FACEBOOK = (By.CSS_SELECTOR, "footer a[href*='facebook.com']")
    FOOTER_SOCIAL_MEDIA_INSTAGRAM = (By.CSS_SELECTOR, "footer a[href*='instagram.com']")
    FOOTER_SOCIAL_MEDIA_GOOGLE = (By.CSS_SELECTOR, "footer a[href*='g.page']")
    FOOTER_SOCIAL_MEDIA_TWITTER = (By.CSS_SELECTOR, "footer a[href*='twitter.com']")

    FOOTER_QUICK_LINKS_ABOUT_US = (By.CSS_SELECTOR, "footer a[href*='about']")
    FOOTER_QUICK_LINKS_SERVICES = (By.CSS_SELECTOR, "footer a[href*='services']")
    FOOTER_QUICK_LINKS_APPOINTMENTS = (By.CSS_SELECTOR, "footer a[href*='booking']")
    FOOTER_QUICK_LINKS_CONTACT_US = (By.CSS_SELECTOR, "footer a[href*='contact']")

    FOOTER_SERVICES_PAIN_MANAGEMENT = (By.CSS_SELECTOR, "footer a[href*='pain-management']")
    FOOTER_SERVICES_ELECTRODIAGNOSTICS = (By.CSS_SELECTOR, "footer a[href*='electrodiagnostic']")
    FOOTER_SERVICES_IME = (By.CSS_SELECTOR, "footer a[href*='independent-medical-exams']")
    FOOTER_SERVICES_PLATELET_RICH_PLASMA = (By.CSS_SELECTOR, "footer a[href*='platelet-rich-plasma-prp']")
    FOOTER_SERVICES_INFUSION_THERAPY = (By.CSS_SELECTOR, "footer a[href*='infusion-therapy']")
    FOOTER_SERVICES_LIFESTYLE_MEDICINE = (By.CSS_SELECTOR, "footer a[href*='lifestyle-medicine']")
    FOOTER_PRIVACY_POLICY = (By.CSS_SELECTOR, "footer a[href*='privacy-policy']")
    FOOTER_TERMS_AND_CONDITIONS = (By.CSS_SELECTOR, "footer a[href*='terms']")

    def __init__(self, driver):
        # Transfer the driver and wait from the parent
        super().__init__(driver) 

 


  
  




    