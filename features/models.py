from pytest_bdd import scenario, given, when, then


@given("a create order request")
def step_impl():
    raise NotImplementedError(u'STEP: Given a create order request')


@when("I serialize the object")
def step_impl():
    raise NotImplementedError(u'STEP: When I serialize the object')


@then("the order request is converted to a dictionary properly")
def step_impl():
    raise NotImplementedError(u'STEP: Then the order request is converted to a dictionary properly')


@given("an OrderDetail with order_number = 123, order_price = 10000, month_installment = 6")
def step_impl():
    raise NotImplementedError(
        u'STEP: Given an OrderDetail with order_number = 123, order_price = 10000, month_installment = 6')


@then("the OrderDetail is serialized correctly")
def step_impl():
    raise NotImplementedError(u'STEP: Then the OrderDetail is serialized correctly')