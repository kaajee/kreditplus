from pytest_bdd import scenario, given, when, then


@given("an object OrderRequest")
def step_impl():
    context.order_request = NewOrderRequest(
        order_number='1001',
        order_price='600000',
        month_installment='6',
        name='kevin',
        ktp_number='1234567890123456',
        birthdate='01 Januari 1992',
        address='Jalan Palmerah Barat',
        mobile_phone='087812345678',
        phone='1234567',
        office_name='Kompas Gramedia',
        office_phone='1234567',
        sibling_name='Budi',
        sibling_phone='1234567'
    )


@when("I make a succesfull new order request")
def step_impl():
    context.response_order_id = context.gateway.create_order(
        context.order_request
    )

    patcher.stop()


@then('i get string "ok"')
def step_impl():
    assert context.response == ok

