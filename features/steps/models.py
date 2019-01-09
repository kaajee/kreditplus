# from behave import *
#
# from kreditplus.models import NewOrderRequest
#
#
# @given("a create order request")
# def step_impl(context):
#     ontext.entity = NewOrderRequest(
#         order_number = '1001',
#         order_price = '600000',
#         month_installment = '6',
#         name = 'kevin',
#         ktp_number = '1234567890123456',
#         birthdate = '01 Januari 1992',
#         address = 'Jalan Palmerah Barat',
#         mobile_phone = '087812345678',
#         phone = '1234567',
#         office_name = 'Kompas Gramedia',
#         office_phone = '1234567',
#         sibling_name = 'Budi',
#         sibling_phone = '1234567'
#     )
#
#
# @when("I serialize the object")
# def step_impl(context):
#     context.serialized = context.entity.serialize()
#
#
# @then("the order request is converted to a dictionary properly")
# def step_impl(context):
#     assert context.serialized == (
#         f'[{{"order_code": "{context.entity.order_number}", '
#         f'"order_price": "{context.entity.order_price}", '
#         f'"month_installment": {context.entity.month_installment}, '
#     ), f'context.serialized was {context.serialized}'