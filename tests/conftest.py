import logging
import pytest
from datetime import datetime
from selenium import webdriver
from pytest_html import extras
import base64
import os
from selenium.webdriver.chrome.options import Options
from pages.home import HomePage  # Import specific pages
from utils.custom_logger import LogGen

@pytest.fixture
def home(driver):
    """Initializes HomePage. This automatically triggers BasePage's __init__."""
    return HomePage(driver)

@pytest.fixture
def services(driver):
    from pages.services import ServicesPage
    return ServicesPage(driver)

@pytest.fixture
def about(driver):
    from pages.about import AboutPage
    return AboutPage(driver)

@pytest.fixture
def contact(driver):
    from pages.contact import ContactPage
    return ContactPage(driver)

@pytest.fixture
def pain_management(driver):
    from pages.pain_management import PainManagementPage
    return PainManagementPage(driver)

@pytest.fixture
def electro_diagnostics(driver):
    from pages.electrodiagnostics import ElectroDiagnosticsPage
    return ElectroDiagnosticsPage(driver)

@pytest.fixture
def ime(driver):
    from pages.ime import ImePage
    return ImePage(driver)

@pytest.fixture
def infusion_therapy(driver):
    from pages.infusion_therapy import InfusionTherapyPage
    return InfusionTherapyPage(driver)  

@pytest.fixture
def prp(driver):
    from pages.prp import PrpPage
    return PrpPage(driver)

@pytest.fixture
def lifestyle_medicine(driver):
    from pages.lifestyle_medicine import LifestyleMedicinePage
    return LifestyleMedicinePage(driver)

@pytest.fixture(scope="function")
def setup_logger(request):
    for fixture_value in request.node.funcargs.values():
        if hasattr(fixture_value, "logger"):
            request.cls.logger = fixture_value.logger
            return
            
    # IMPROVED FALLBACK: If no page object is found, create an adapter with "Test" as the name
    raw_logger = LogGen.loggen()
    request.cls.logger = logging.LoggerAdapter(raw_logger, {"page_name": "TestContext"})



# Enhanced driver fixture with stealth settings to avoid detection by anti-automation scripts.
@pytest.fixture(scope="function")
def driver(request):
    """Initializes and tears down the Selenium WebDriver with stealth settings."""
    chrome_options = Options()
    
     # NEW: Check if running in GitHub Actions CI
    if os.environ.get('GITHUB_ACTIONS') == 'true':
        chrome_options.add_argument("--headless=new") # Modern headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080") # maximize_window() doesn't always work in headless
    
    # Enable all levels of browser logging
    # Note: capabilities are moving to 'options' in newer Selenium versions
    chrome_options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

    # 1. Hide the "controlled by automated test software" banner
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # 2. Set a real User-Agent to mimic a human browser
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=chrome_options)
    
    # 3. CRITICAL: Nullify the 'webdriver' property in the browser's memory
    # This prevents security scripts from detecting 'navigator.webdriver = true'
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    })
    
     # Only maximize if not in headless (headless uses --window-size above)
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        driver.maximize_window()
    
    yield driver
    
    driver.quit()

# This is the original driver fixture that initializes and tears down the Selenium WebDriver.
# @pytest.fixture(scope="function")
# def driver(request):
#     """Initializes and tears down the Selenium WebDriver."""
#     # Setup: Start the browser (Chrome example)
#     driver = webdriver.Chrome()
#     driver.maximize_window()
    
#     # Provide the driver instance to the test
#     yield driver    # yield splits setup and teardown.  Code before yield is setup, code after is teardown.
    
#     # Teardown: Close the browser after the test completes
#     driver.quit()

# The following hook modifies the title of the HTML report
def pytest_html_report_title(report):
    '''Modify the title and main heading of the HTML report.'''
    report.title = "California Pain & Regenerative Medicine Institute - Test Report"

# The following hook adds a custom logo to the HTML report
def pytest_html_results_summary(prefix):
    """Injects the logo with a specific ID for CSS repositioning."""
    logo_path = os.path.join(os.getcwd(), "JMHMD-white-350x67.png")
    
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        
        # We give the div an ID of 'custom-logo'
        logo_html = f'''
            <div id="custom-logo">
                <img src="data:image/png;base64,{encoded_string}" 
                     style="height:60px; width:auto;">
            </div>
        '''
        prefix.extend([logo_html])

# Version - 0

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # --- PART 1: Save Isolated Screenshot with Meaningful Name ---
            # Create directory if it doesn't exist
            scr_dir = os.path.join(os.getcwd(), "logs", "screenshots")
            os.makedirs(scr_dir, exist_ok=True)
            
            # Create a unique, descriptive filename
            test_name = item.name
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_path = os.path.join(scr_dir, f"FAILED_{test_name}_{timestamp}.png")
            
            # Save the physical file
            driver.save_screenshot(file_path)

            # --- PART 2: Embed in HTML Report ---
            screenshot_base64 = driver.get_screenshot_as_base64()
            report.extras = getattr(report, "extras", [])
            # You can even use the descriptive name in the report link!
            report.extras.append(extras.png(screenshot_base64, name=f"Fail: {test_name}"))

# Version - 1
# --------------------------------------------------------------------------------------------------------------------------------------
# Initial hook version to capture screenshots on failure.  This version adds a static small image to the report next to the failed test.
# In order to see a larger image, right click the image and click on "Open image to open in a new tab".
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
    
#     # Hook to capture a screenshot on test failure and embed it in the HTML report.
    
#     outcome = yield
#     report = outcome.get_result()
    
#     # Check if the test failed during the actual test 'call' phase
#     if report.when == "call" and report.failed:
#         # Retrieve the 'driver' fixture from the test item
#         driver = item.funcargs.get("driver")
#         if driver:
#             # Capture screenshot as a base64 string for a self-contained report
#             screenshot_base64 = driver.get_screenshot_as_base64()
#             # Simplified static large image
     
#             # Use 'extras' to add the image to the report
#             # Ensure report.extras exists to avoid errors in newer pytest-html versions
#             report.extras = getattr(report, "extras", [])
#             report.extras.append(extras.png(screenshot_base64, name="Screenshot on Failure"))

# Version - 2
# --------------------------------------------------------------------------------------------------------------------------------------
#  Improved hook version to capture screenshots on failure.  This version adds a larger image (medium size) directly visible in the report.
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """
#     Hook to capture a screenshot on test failure and embed it in the HTML report.
#     """
#     outcome = yield
#     report = outcome.get_result()
    
#     # Check if the test failed during the actual test 'call' phase
#     if report.when == "call" and report.failed:
#         # Retrieve the 'driver' fixture from the test item
#         driver = item.funcargs.get("driver")
#         if driver:
#             # Capture screenshot as a base64 string for a self-contained report
#             screenshot_base64 = driver.get_screenshot_as_base64()
#             # Simplified static large image
#             screenshot_b64 = driver.get_screenshot_as_base64()
#             html = f'<div><img src="data:image/png;base64,{screenshot_b64}" style="width:100%; max-width:800px; border:2px solid #000; margin-top:10px;"/></div>'

#             report.extras = getattr(report, "extras", [])
#             report.extras.append(extras.html(html))


# Version - 3
# --------------------------------------------------------------------------------------------------------------------------------------
# Version with clickable image to enlarge
# ---------------------------------------
# The following hood is a more advanced version that allows clicking to enlarge the image
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
    
#     if report.when == 'call' and report.failed:
#         driver = item.funcargs.get('driver')
#         if driver:
#             screenshot_b64 = driver.get_screenshot_as_base64()
            
#             # Simple JavaScript to toggle image size between 300px and 100%
#             html = f'''
#             <div>
#                 <img src="data:image/png;base64,{screenshot_b64}" 
#                      alt="Failure Screenshot" 
#                      style="width:300px; cursor:zoom-in; border:1px solid #ddd; transition: 0.3s;" 
#                      onclick="if(this.style.width=='300px'){{this.style.width='100%'; this.style.cursor='zoom-out';}}else{{this.style.width='300px'; this.style.cursor='zoom-in';}}"
#                      align="right"/>
#             </div>'''
            
#             report.extras = getattr(report, "extras", [])
#             report.extras.append(extras.html(html))




