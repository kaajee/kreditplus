from behave import *

from kreditplus.models import NewOrderRequest, OrderDetail


@given("a create order request")
def step_impl(context):
    context.entity = NewOrderRequest(
        full_name='kevin',
        id_card_no='123567890123456',
        birth_date='01 January 1992',
        address='Jalan Palmerah Barat',
        handphone='08123456789',
        phone='1234567',
        office_name='Kompas Gramedia',
        office_phone='1234567',
        sibling_name='Budi',
        sibling_phone='1234567',
        details=OrderDetail(
            ref_number='10001',
            total_price=3000000,
            product_name='Spring Bed Comforta White - Quee',
            receiver_name='Ghia Anandea',
            receiver_address='Jl. Parung Panjang',
            tenor_instalment=12,
        ).serialize()
    )


@when("I serialize the object")
def step_impl(context):
    context.serialized = context.entity.serialize()


@then("the order request is converted to a dictionary properly")
def step_impl(context):
    assert context.serialized == {
        "fullName": context.entity.full_name,
        "idCardNo": context.entity.id_card_no,
        "birthDate": context.entity.birth_date,
        "address": context.entity.address,
        "handphone": context.entity.handphone,
        "phone": context.entity.phone,
        "office_name": context.entity.office_name,
        "office_phone": context.entity.office_phone,
        "sibling_name": context.entity.sibling_name,
        "sibling_phone": context.entity.sibling_phone,
        "details": context.entity.details
    }


@given("an OrderDetail with ref_number = {ref_number}, total_price = {total_price}, productName = {product_name}, "
       "receiver_name = {receiver_name}, receiver_address = {receiver_address}, tenor_instalment = {tenor_instalment}")
def step_impl(context, ref_number, total_price, product_name, receiver_name, receiver_address, tenor_instalment):
    context.entity = OrderDetail(
        ref_number=ref_number,
        total_price=total_price,
        product_name=product_name,
        receiver_name=receiver_name,
        receiver_address=receiver_address,
        tenor_instalment=tenor_instalment
    )


@then("the OrderDetail is serialized correctly")
def step_impl(context):
    assert context.serialized == (
        f'[{{"refNo": "{context.entity.ref_number}", '
        f'"totalPrice": {context.entity.total_price}, '
        f'"productName": "{context.entity.product_name}", '
        f'"receiverName": "{context.entity.receiver_name}",'
        f'"receiverAddress": "{context.entity.receiver_address}",'
        f'"tenorInstalment": {context.entity.tenor_instalment}}}]'
    ), f'context.serialized was {context.serialized}'


@step("a valid order request")
def step_impl(context):
    context.order_request = NewOrderRequest(
        full_name='Kevin',
        id_card_no='123567890123456',
        birth_date='01 January 1992',
        address='Jalan Palmerah Barat',
        handphone='08123456789',
        phone='1234567',
        office_name='Kompas Gramedia',
        office_phone='1234567',
        sibling_name='Budi',
        sibling_phone='1234567',
        details=OrderDetail(
            ref_number='10001',
            total_price=3000000,
            product_name='Spring Bed Comforta White - Quee',
            receiver_name='Ghia Anandea',
            receiver_address='Jl. Parung Panjang',
            tenor_instalment=12,
        ).serialize()
    )


@then("i get success response")
def step_impl(context):
    assert context.response["status"] == 'success'


@then("i get error response")
def step_impl(context):
    assert context.response["status"] == 'error'


@when("i validate order request")
def step_impl(context):
    context.response = context.order_request.input_validation(context.order_request)


@step("a invalid order request")
def step_impl(context):
    context.order_request = NewOrderRequest(
        full_name='Kevin',
        id_card_no='123567890123456',
        birth_date='01 January 1992',
        address='Jalan Palmerah Barat',
        handphone='1234567',
        phone='1234567',
        office_name='Kompas Gramedia',
        office_phone='asdad',
        sibling_name='Budi',
        sibling_phone='asdad',
        details=OrderDetail(
            ref_number='10001',
            total_price=3000000,
            product_name='Spring Bed Comforta White - Quee',
            receiver_name='Ghia Anandea',
            receiver_address='Jl. Parung Panjang',
            tenor_instalment=12,
        ).serialize()
    )
