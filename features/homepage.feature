Feature: Homepage

  Scenario: Redirect to Authentication
    Given I am on the Homepage
    When I click on 'Form Authentication' link
    Then  I am redirected to Login Page