Feature: Food donation request system
  Scenario: Successful donation request
    Given a registered community member
    When the member submits a request for 2 food parcels
    Then the request should be approved
  Scenario: Request exceeds donation limit
    Given a registered community member
    When the member submits a request for 10 food parcels
    Then the request should be rejected
  Scenario: Invalid user request
    Given an unregistered user
    When the user submits a request for 1 food parcel
    Then an error message should be displayed