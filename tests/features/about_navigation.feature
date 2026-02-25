Feature: About Page Navigation

  Scenario: User navigates to the booking page from About Us
    Given the user is on the "About" page
    When the user clicks the "Appointment" button
    Then the browser should open a new tab with "booking" in the URL
