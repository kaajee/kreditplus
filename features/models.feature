Feature: Request Serialization

  Scenario: Create NewOrder in form html
    Given a create order request
    When I serialize the object
    Then the order request is converted to a dictionary properly

  Scenario: Create NewOrder in form html
    Given a create order request
    When I make a valid order request
    Then i get Success response

  Scenario: Create NewOrder in form html
    Given a create order request
    When I make a invalid order request
    Then i get Error response

#  Scenario: Save order request
#    Given a create order request
#    When I submit order request
#    Then the order request is saved to database