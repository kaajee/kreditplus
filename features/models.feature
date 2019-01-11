Feature: Request Serialization

  Scenario: Create NewOrder in form html
    Given a create order request
    When I serialize the object
    Then the order request is converted to a dictionary properly
