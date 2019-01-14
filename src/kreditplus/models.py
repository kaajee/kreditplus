"""
Models
======
Represent data that is sent to the the KreditPlus.
"""

# from kreditplus.exceptions import KreditPlusError

__all__ = ['OrderDetail', 'NewOrderRequest']


class OrderDetail:
    """ An order line item (generally as part of a `NewOrderRequest`)
    """
    def __init__(self, ref_number, total_price, product_name, receiver_name, receiver_address, tenor_instalment,):
        """
        :param `str` ref_number: A product SKU for one of the line items that was ordered.
        :param `int` total_price: The total price of order.
        :param `str` product_name: The human-readable name of the product that was ordered.
        :param `str` receiver_name: Recipient name.
        :param `str` receiver_address: Recipient address.
        :param `int` tenor_instalment: The number of tenor installment.
        """
        self.ref_number = ref_number
        self.total_price = total_price
        self.product_name = product_name
        self.receiver_name = receiver_name
        self.receiver_address = receiver_address
        self.tenor_instalment = tenor_instalment

    def serialize(self):
        """ Converts this object to a string representation, suitable for sending to the AkuLaku API.

        :return: A string representation of this instance.
        :rtype: str
        """
        return (f'[{{"refNo": "{self.ref_number}", '
                f'"totalPrice": {self.total_price}, '
                f'"productName": "{self.product_name}", '
                f'"receiverName": "{self.receiver_name}",'
                f'"receiverAddress": "{self.receiver_address}",'
                f'"tenorInstalment": {self.tenor_instalment}}}]')


class NewOrderRequest:
    """ An order which is sent to the KreditPlus.
    """
    def __init__(self,
                 full_name,
                 id_card_no,
                 birth_date,
                 address,
                 handphone,
                 phone,
                 office_name,
                 office_phone,
                 sibling_name,
                 sibling_phone,
                 details):
        self.full_name = full_name
        self.id_card_no = id_card_no
        self.birth_date = birth_date
        self.address = address
        self.handphone = handphone
        self.phone = phone
        self.office_name = office_name
        self.office_phone = office_phone
        self.sibling_name = sibling_name
        self.sibling_phone = sibling_phone
        self.details = details if type(details) is str else details.serialize()

    # @property
    # def content(self):
    #     """ Generates a stringified version of this object not for API consumption, but for generating signatures.
    #     :rtype: str
    #     """
    #     required_attributes = [
    #         'full_name', 'id_card_no', 'birth_date', 'address', 'handphone', 'phone', 'office_name', 'office_phone',
    #         'sibling_name', 'details'
    #     ]
    #     return ''.join([getattr(self, attr) for attr in required_attributes])

    def serialize(self):
        """ Converts this object to a dictionary, suitable for serializing in an HTTP request.
        :return: A dictionary that representation of this class
        :rtype: dict
        """
        return {
            "fullName": self.full_name,
            "idCardNo": self.id_card_no,
            "birthDate": self.birth_date,
            "address": self.address,
            "handphone": self.handphone,
            "phone": self.phone,
            "office_name": self.office_name,
            "office_phone": self.office_phone,
            "sibling_name": self.sibling_name,
            "sibling_phone": self.sibling_phone,
            "details": self.details,
        }

    @staticmethod
    def input_validation(order_request):

        # Get Order request
        data = order_request.serialize()

        not_null_key = ["id_card_no", "birth_date", "address", "handphone", "phone", "office_name", "office_phone",
                        "sibling_phone"]
        digit_key = ["id_card_no", "phone", "office_phone", "sibling_phone"]

        # Looping request data
        for key, value in data.items():

            # Check if value is null
            if key in not_null_key:
                if value is None:
                    return {
                        "status": "error",
                        "message": f"{key} must not null!"
                    }

            # Check if value is digit
            if key in digit_key:
                if not value.isdigit():
                    return {
                        "status": "error",
                        "message": f"{key} must be a digit!"
                    }

        return {
            "status": "success",
            "message": ""
        }

    # def send_order(self, order_request):
        # TODO:
        #   1. Setup mail connection
        #   2. Create email body for order
        #   3. Send order request
