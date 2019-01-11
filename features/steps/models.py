from behave import *

from kreditplus.models import NewOrderRequest


@given("a create order request")
def step_impl(context):
    context.entity = NewOrderRequest(
        ref_number='10001',
        total_price='3.000.000',
        product_name='Spring Bed Comforta White - Quee',
        receiver_name='Ghia Anandea',
        receiver_address='Jl. Parung Panjang, No 17A, Kec. Parung, Kab. Bogor - Jawa Barat',
        tenor_instalment='12',
        full_name='kevin',
        id_card_no='123567890123456',
        birth_date='01 January 1992',
        address='Jalan Palmerah Barat',
        handphone='08123456789',
        email='087812345678',
    )


@when("I serialize the object")
def step_impl(context):
    context.serialized = context.entity.serialize()


@then("the order request is converted to a dictionary properly")
def step_impl(context):
    assert context.serialized == {
        "refNo": context.entity.ref_number,
        "totalPrice": context.entity.total_price,
        "productName": context.entity.product_name,
        "receiverName": context.entity.receiver_name,
        "receiverAddress": context.entity.receiver_address,
        "tenorInstalment": context.entity.tenor_instalment,
        "fullName": context.entity.full_name,
        "idCardNo": context.entity.id_card_no,
        "birthDate": context.entity.birth_date,
        "address": context.entity.address,
        "handphone": context.entity.handphone,
        "email": context.entity.email
    }