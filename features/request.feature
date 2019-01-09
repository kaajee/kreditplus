Feature: Kreditplus Request
  # Enter feature description here

  Scenario: Create new order request for KreditPlus
    Given an object OrderRequest
    When I make a succesfull new order request
    Then i get string "ok"