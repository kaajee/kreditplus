# from pytest_bdd import scenario, given, when, then
from behave import *
from kreditplus.models import NewOrderRequest


@given("a create order request")
def step_impl(context):
    context.entity = NewOrderRequest(
        order_number='1001',
        order_price='600000',
        month_installment='6',
        name='kevin',
        ktp_number='123567890123456',
        birth_date='01 January 1992',
        address='Jalan Palmerah Barat',
        mobile_phone='087812345678',
        phone='1234567',
        office_name='Kompas Gramedia',
        office_phone='1234567',
        sibling_name='Budi',
        sibling_phone='1234567'
    )


@when("I serialize the object")
def step_impl(context):
    context.serialized = context.entity.serialize()


@then("the order request is converted to a dictionary properly")
def step_impl(context):
    assert context.entity, "Order is required"
    assert context.serialized == {
        "order_number": context.entity.order_number,
        "order_price": context.entity.order_price,
        "month_installment": context.entity.month_installment,
        "name": context.entity.name,
        "ktp_number": context.entity.ktp_number,
        "birth_date": context.entity.birth_date,
        "address": context.entity.address,
        "mobile_phone": context.entity.mobile_phone,
        "phone": context.entity.phone,
        "office_name": context.entity.office_name,
        "office_phone": context.entity.office_phone,
        "sibling_name": context.entity.sibling_name,
        "sibling_phone": context.entity.sibling_phone
    }

