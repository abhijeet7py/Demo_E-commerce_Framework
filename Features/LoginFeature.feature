Feature: Login to Swag
  Scenario: Check Successful Login
    Given Launch the Browser
    When Open Swag Website
    And Enter Username "standard_user" and Password "secret_sauce"
    Then Verify Homepage URL
