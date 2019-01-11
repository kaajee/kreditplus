from behave import *

from kreditplus.models import NewOrderRequest, KreditPlusError


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
        phone='1234567',
        office_name='Kompas Gramedia',
        office_phone='1234567',
        sibling_name='Budi',
        sibling_phone='1234567'
    )


@when("I serialize the object")
def step_impl(context):
    context.serialized = context.entity.serialize


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
        "phone": context.entity.phone,
        "office_name": context.entity.office_name,
        "office_phone": context.entity.office_phone,
        "sibling_name": context.entity.sibling_name,
        "sibling_phone": context.entity.sibling_phone
    }


@when("I make a valid order request")
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
        phone='1234567',
        office_name='Kompas Gramedia',
        office_phone='1234567',
        sibling_name='Budi',
        sibling_phone='1234567'
    )

    context.validation = context.entity.validation


@then("i get Success response")
def step_impl(context):
    assert context.validation == 'Success'


@when("I make a invalid order request")
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
        handphone='abcd',
        phone='abcd',
        office_name='Kompas Gramedia',
        office_phone='1234567',
        sibling_name='Budi',
        sibling_phone='abcd'
    )

    context.validation = context.entity.validation


@then("i get Error response")
def step_impl(context):
    assert context.validation == 'Error'
