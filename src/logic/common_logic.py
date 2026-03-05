from selenium.webdriver.support import expected_conditions as EC

class CommonLogic:

    @staticmethod
    def is_valid_phone_format(phone_text):
        """Standard verification for all phone numbers across the site."""
        clean_phone = "".join(filter(str.isdigit, phone_text))
        return len(clean_phone) >= 10


    @staticmethod
    def is_valid_address(address_text):
        """Standard check for regional office data (Encino/91436)."""
        address_upper = address_text.upper()
        return "91436" in address_upper or "ENCINO" in address_upper


    @staticmethod
    def verify_link_flow(page, locator, expected_slug="booking", click_type="safe", scroll=True):
        """Unified flow for link verification across the entire site."""
        page.logger.info(f"Starting unified flow for {page.__class__.__name__} | Click: {click_type}")
        
        page.navigate()

        if scroll:
            page.scroll_to_element(locator)

        click_map = {
            "safe": page.safe_click,
            "force": page.force_click,
            "quick": page.quick_click,
            "actions": page.click_with_actions
        }
        
        # Use the strategy pattern to select the click method
        action = click_map.get(click_type, page.safe_click)
        action(locator)

        page.handle_external_tab()
        
        try:
            page.wait.until(EC.url_contains(expected_slug))
            page.logger.info(f"Successfully reached {expected_slug}")
        except Exception as e:
            actual = page.driver.current_url
            page.logger.error(f"URL Mismatch! Expected: {expected_slug} | Actual: {actual}")
            raise e