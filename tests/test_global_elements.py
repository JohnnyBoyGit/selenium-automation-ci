# tests/test_global_elements.py
import time
import pytest
from pages.home import HomePage

@pytest.mark.parametrize("menu_locator", [
    "SITE_LOGO",
    "HOME_MENU_ITEM",
    "ABOUT_MENU_ITEM",
    "SERVICES_MENU_ITEM",
    "CONTACT_MENU_ITEM"
])

def test_header_menu_links(driver, menu_locator):
    home_page = HomePage(driver)
    home_page.navigate()
    
    # Point getattr to the header component, where these locators live
    # It is recommended to add a default value of None to the locator below like locator = getattr(home_page.header, menu_locator, None).  
    # This way, it returns None if the attribute is missing, instead of crashing
    locator = getattr(home_page.header, menu_locator)
    assert home_page.header.element_is_visible(locator), f"{menu_locator} is not visible"

@pytest.mark.parametrize("submenu_locator", [
    "SERVICES_SUBMENU_PAIN_MANAGEMENT",
    "SERVICES_SUBMENU_ELECTRODIAGNOSTICS",
    "SERVICES_SUBMENU_INDEPENDENT_MEDICAL_EXAMS",
    "SERVICES_SUBMENU_INFUSION_THERAPY",
    "SERVICES_SUBMENU_PLATELET_RICH_PLASMA_PRP",
    "SERVICES_SUBMENU_LIFESTYLE_MEDICINE"
])

def test_header_submenu_links(driver, submenu_locator):
    home_page = HomePage(driver)
    home_page.navigate()
    
    # 1. HOVER over the parent 'Services' menu first to trigger the submenu
    # home_page.header.SERVICES_MENU_ITEM is the parent
    home_page.header.hover(home_page.header.SERVICES_MENU_ITEM)
    time.sleep(0.5) # brief pause to allow submenu to appear    
     # 2. Get the specific submenu locator dynamically
    locator = getattr(home_page.header, submenu_locator)
    # 3. NOW assert visibility (it should be True now that we hovered)
    assert home_page.header.element_is_visible(locator), f"{submenu_locator} is not visible"


@pytest.mark.parametrize("footer_social_locator", [
    "FOOTER_SOCIAL_MEDIA_FACEBOOK",
    "FOOTER_SOCIAL_MEDIA_INSTAGRAM",
    "FOOTER_SOCIAL_MEDIA_GOOGLE",
    "FOOTER_SOCIAL_MEDIA_TWITTER"
])

def test_footer_social_links(driver, footer_social_locator):
    home_page = HomePage(driver)
    home_page.navigate()
    
    locator = getattr(home_page.footer, footer_social_locator)
    # Use your new dynamic scroll method
    home_page.scroll_to_element(locator)
    assert home_page.footer.element_is_visible(locator), f"{footer_social_locator} is not visible"

@pytest.mark.parametrize("footer_quick_links_locator", [
    "FOOTER_QUICK_LINKS_ABOUT_US",
    "FOOTER_QUICK_LINKS_SERVICES",
    "FOOTER_QUICK_LINKS_APPOINTMENTS",
    "FOOTER_QUICK_LINKS_CONTACT_US"
])

def test_footer_quick_links(driver, footer_quick_links_locator):
    home_page = HomePage(driver)
    home_page.navigate()
    
    locator = getattr(home_page.footer, footer_quick_links_locator)
    # Use your new dynamic scroll method
    home_page.scroll_to_element(locator)
    assert home_page.footer.element_is_visible(locator), f"{footer_quick_links_locator} is not visible"

@pytest.mark.parametrize("footer_services_locator", [
    "FOOTER_SERVICES_PAIN_MANAGEMENT",
    "FOOTER_SERVICES_ELECTRODIAGNOSTICS",
    "FOOTER_SERVICES_IME",
    "FOOTER_SERVICES_PLATELET_RICH_PLASMA",    
    "FOOTER_SERVICES_INFUSION_THERAPY",
    "FOOTER_SERVICES_LIFESTYLE_MEDICINE"
])

def test_footer_services_links(driver, footer_services_locator):
    home_page = HomePage(driver)
    home_page.navigate()
    
    locator = getattr(home_page.footer, footer_services_locator)
    # Use your new dynamic scroll method
    home_page.scroll_to_element(locator)
    assert home_page.footer.element_is_visible(locator), f"{footer_services_locator} is not visible"

@pytest.mark.parametrize("footer_policy_term_locator", [
    "FOOTER_PRIVACY_POLICY",
    "FOOTER_TERMS_AND_CONDITIONS"
])

def test_footer_policy_term_links(driver, footer_policy_term_locator):
    home_page = HomePage(driver)
    home_page.navigate()
    
    locator = getattr(home_page.footer, footer_policy_term_locator)
    # Use your new dynamic scroll method
    home_page.scroll_to_element(locator)
    assert home_page.footer.element_is_visible(locator), f"{footer_policy_term_locator} is not visible"