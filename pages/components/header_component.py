from selenium.webdriver.common.by import By
from pages.base import BasePage

class HeaderComponent(BasePage):

    # Locators stored as tuples
    SITE_LOGO = (By.CSS_SELECTOR, "[class='custom-logo-link transparent-custom-logo'] img")
    HOME_MENU_ITEM = (By.CSS_SELECTOR, "#menu-item-19 a")
    ABOUT_MENU_ITEM = (By.CSS_SELECTOR, "#menu-item-20 a")
    SERVICES_MENU_ITEM = (By.CSS_SELECTOR, "#menu-item-21 a")
    CONTACT_MENU_ITEM = (By.CSS_SELECTOR, "#menu-item-23 a")

    # This looks for any link inside the submenu that contains the word 'pain-management'
    SERVICES_SUBMENU_PAIN_MANAGEMENT = (By.CSS_SELECTOR, "ul.sub-menu  a[href*='pain-management']")   
    SERVICES_SUBMENU_ELECTRODIAGNOSTICS = (By.CSS_SELECTOR, "ul.sub-menu a[href*='electrodiagnostic']")
    SERVICES_SUBMENU_INDEPENDENT_MEDICAL_EXAMS = (By.CSS_SELECTOR, "ul.sub-menu  a[href*='independent-medical-exams']")
    SERVICES_SUBMENU_INFUSION_THERAPY = (By.CSS_SELECTOR, "ul.sub-menu a[href*='infusion-therapy']")
    SERVICES_SUBMENU_PLATELET_RICH_PLASMA_PRP = (By.CSS_SELECTOR, "ul.sub-menu a[href*='platelet-rich-plasma-prp']")
    SERVICES_SUBMENU_LIFESTYLE_MEDICINE = (By.CSS_SELECTOR, "ul.sub-menu a[href*='lifestyle-medicine']")

    def __init__(self, driver):
        # Transfer the driver and wait from the parent
        super().__init__(driver) 

    