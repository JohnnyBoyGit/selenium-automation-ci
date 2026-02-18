from selenium import webdriver
from selenium.webdriver.common.by import By
import collections

def generate_unique_locators(url):
    driver = webdriver.Chrome()
    driver.get(url)
    
    # Target only interactive elements to reduce noise
    elements = driver.find_elements(By.XPATH, "//button | //input | //a | //select | //textarea")
    
    # Dictionary to track duplicate XPaths for indexing
    xpath_counts = collections.defaultdict(int)
    
    print(f"\n{'LABEL/TEXT':<30} | {'TAG':<10} | {'UNIQUE LOCATOR'}")
    print("-" * 90)

    for element in elements:
        try:
            if not element.is_displayed(): continue
            
            tag = element.tag_name
            label = (element.text or element.get_attribute("placeholder") or 
                     element.get_attribute("aria-label") or "No_Label").strip()[:30]
            
            # Attributes for Priority Logic
            eid = element.get_attribute("id")
            testid = element.get_attribute("data-testid") or element.get_attribute("data-qa")
            ename = element.get_attribute("name")

            # 1. PRIORITY: ID (Highest stability)
            if eid and not eid.isdigit(): # Skip purely numeric dynamic IDs
                locator = f"(By.ID, '{eid}')"
            
            # 2. PRIORITY: Custom Test Attributes (Standard for 2026)
            elif testid:
                locator = f"(By.CSS_SELECTOR, '[data-testid=\"{testid}\"]')"
            
            # 3. PRIORITY: Name
            elif ename:
                locator = f"(By.NAME, '{ename}')"
            
            # 4. FALLBACK: Indexed XPath (Ensures uniqueness)
            else:
                base_xpath = f"//{tag}[contains(text(), '{label[:15]}')]" if label != "No_Label" else f"//{tag}"
                xpath_counts[base_xpath] += 1
                count = xpath_counts[base_xpath]
                # If it's a duplicate, add the [index]
                locator = f"(By.XPATH, '({base_xpath})[{count}]')"

            print(f"{label:<30} | {tag:<10} | {locator}")

        except:
            continue
    driver.quit()

generate_unique_locators("https://calipain.com/")
