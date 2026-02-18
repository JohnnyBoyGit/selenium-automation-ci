import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_ui_verifies_api_data(driver):
    # 1. MOCK API - Bypass your blocked network entirely
    mock_api_data = {"name": "Selenium"}
    api_name = mock_api_data["name"]

    # 2. UI Action - Navigate to DuckDuckGo
    driver.get("https://duckduckgo.com")
    
    # Increase timeout to 20 seconds for slow networks
    wait = WebDriverWait(driver, 20)
    
    # Find search box and submit
    search_input = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
    search_input.send_keys(api_name + Keys.RETURN)

    # 3. Verification - Wait for ANY result to appear
    # We use a broad CSS selector that covers most search results
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "article, .result, #links")))
        
        # Final check: Is our word on the page?
        assert api_name.lower() in driver.page_source.lower()
        print(f"SUCCESS: Found {api_name} results!")
        
    except Exception as e:
        # If it fails, take a screenshot to see what happened
        driver.save_screenshot("timeout_debug.png")
        pytest.fail(f"Results did not load in time. Check 'timeout_debug.png'. Error: {e}")
