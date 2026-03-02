import os
import pytest
from pytest_bdd import scenario, given, when, then
from src.logic.about_logic import AboutLogic

# 1. Correct Path: 'features' is in the same folder as this file
FEATURE_FILE = os.path.join(os.path.dirname(__file__), "features", "about_navigation.feature")

# 2. Link the scenario to a test function (Crucial for Pytest to run it)
@scenario(FEATURE_FILE, 'User navigates to the booking page from About Us')
def test_navigation_to_booking_page():
    pass

@given('the user is on the "About" page')
def go_to_about(about):
    about.navigate()

@when('the user clicks the "Appointment" button')
def click_appointment(about):
    # Ensure 'about' fixture provides access to the driver and locators
    locator = about.BUTTON_BOOK_AN_APPOINTMENT
    about.force_click(locator)
    about.handle_external_tab()

@then('the browser should open a new tab with "booking" in the URL')
def verify_booking_url(about):
    expected = AboutLogic.get_url_expectation("APPOINTMENT_LINK")
    # Using lower() to stay resilient across different browser URL formatting
    assert expected in about.driver.current_url.lower()
