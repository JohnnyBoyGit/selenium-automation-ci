import json
import pytest
import time
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("endpoint, expected_key, expected_value", [
    ("/users/1", "name", "Leanne Graham"),
    ("/posts/1", "title", "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"),
    ("/todos/1", "title", "delectus aut autem"),
    ("/comments/1", "email", "Eliseo@gardner.biz"),
    ("/albums/1", "title", "quidem molestiae enim"),
    ("/posts/9", "userId", 1),
    ("/posts/23", "title", "maxime id vitae nihil numquam")
])
def test_api_suite_visual(driver, endpoint, expected_key, expected_value):
    """
    Automates 7 API checks by navigating the browser to each endpoint 
    and verifying the JSON content visible on the screen.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    
    # 1. Navigate to the specific endpoint
    driver.get(f"{base_url}{endpoint}")
    
    # 2. Extract the visible text from the browser body
    raw_text = driver.find_element(By.TAG_NAME, "body").text
    
    # 3. Parse JSON
    try:
        api_data = json.loads(raw_text)
    except json.JSONDecodeError:
        pytest.fail(f"Failed to parse JSON at {endpoint}. Browser saw: {raw_text[:50]}")

    # 4. Assertion: Verify the API data matches our expectations
    actual_value = api_data[expected_key]
    assert actual_value == expected_value, f"Expected {expected_value} but got {actual_value}"
    
    print(f"Successfully verified {endpoint}: {expected_key} = {actual_value}")
    
    # Pause for 2 seconds so you can see the data on the screen
    time.sleep(2)
