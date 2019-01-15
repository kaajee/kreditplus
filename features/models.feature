Feature: Request Serialization

  Scenario: OrderDetail serialization
    Given an OrderDetail with ref_number = 123, total_price = 3000000, productName = Spring Bed Comforta White - Quee, receiver_name = Ghia Anandea, receiver_address = Jl. Parung Panjang, No 17A, Kec. Parung, Kab. Bogor - Jawa Barat, tenor_instalment = 12
    When I serialize the object
    Then the OrderDetail is serialized correctly

  Scenario: Create NewOrder in form html
    Given a create order request
    When I serialize the object
    Then the order request is converted to a dictionary properly

  Scenario: Validate order request
    Given an OrderDetail with ref_number = 123, total_price = 3000000, productName = Spring Bed Comforta White - Quee, receiver_name = Ghia Anandea, receiver_address = Jl. Parung Panjang, No 17A, Kec. Parung, Kab. Bogor - Jawa Barat, tenor_instalment = 12
    And a valid order request
    When i validate order request
    Then i get success response

  Scenario: Validate order request
    Given an OrderDetail with ref_number = 123, total_price = 3000000, productName = Spring Bed Comforta White - Quee, receiver_name = Ghia Anandea, receiver_address = Jl. Parung Panjang, No 17A, Kec. Parung, Kab. Bogor - Jawa Barat, tenor_instalment = 12
    And a invalid order request
    When i validate order request
    Then i get error response

  Scenario: Send order request
    Given an EmailData with mail_server = smtp.mydomain.com, mail_port = 587, mail_username = mail@example.com, mail_password = password, from_address = from@example.com, to_address = to@example.com
    And a valid order request
    When i send order request
    Then i get string "true"

#  Scenario: Save order request
#    Given a create order request
#    When I submit order request
#    Then the order request is saved to database