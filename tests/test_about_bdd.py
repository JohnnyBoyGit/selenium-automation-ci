from pytest_bdd import scenario, given, when, then
from src.logic.about_logic import AboutLogic

@scenario('features/about_navigation.feature', 'User navigates to the booking page from About Us')
def test_about_navigation_bdd():
    pass # This stays empty; the decorators do the work

@given('the user is on the "About" page')
def go_to_about(about):
    about.navigate()

@when('the user clicks the "Appointment" button')
def click_appointment(about):
    locator = about.BUTTON_BOOK_AN_APPOINTMENT
    about.force_click(locator)
    about.handle_external_tab()

@then('the browser should open a new tab with "booking" in the URL')
def verify_booking_url(about):
    expected = AboutLogic.get_url_expectation("APPOINTMENT_LINK")
    assert expected in about.driver.current_url.lower()
