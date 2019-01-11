"""
Models
======
Represent data that is sent to the the KreditPlus.
"""

from kreditplus.exceptions import KreditPlusError

__all__ = ['NewOrderRequest']


class NewOrderRequest:
    """ An order which is sent to the KreditPlus.
    """

    def __init__(self,
                 ref_number,
                 total_price,
                 product_name,
                 receiver_name,
                 receiver_address,
                 tenor_instalment,
                 full_name,
                 id_card_no,
                 birth_date,
                 address,
                 handphone,
                 phone,
                 office_name,
                 office_phone,
                 sibling_name,
                 sibling_phone):
        self.ref_number = ref_number
        self.total_price = total_price
        self.product_name = product_name
        self.receiver_name = receiver_name
        self.receiver_address = receiver_address
        self.tenor_instalment = tenor_instalment
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

    @property
    def content(self):
        """ Generates a stringified version of this object not for API consumption, but for generating signatures.
        :rtype: str
        """
        required_attributes = [
            'ref_number', 'total_price', 'product_name', 'receiver_name', 'receiver_address', 'tenor_instalment',
            'full_name', 'id_card_no', 'birth_date', 'address', 'handphone', 'phone', 'office_name', 'office_phone',
            'sibling_name',
        ]
        return ''.join([getattr(self, attr) for attr in required_attributes])

    @property
    def serialize(self):
        """ Converts this object to a dictionary, suitable for serializing in an HTTP request.
        :return: A dictionary that representation of this class
        :rtype: dict
        """
        return {
            "refNo": self.ref_number,
            "totalPrice": self.total_price,
            "productName": self.product_name,
            "receiverName": self.receiver_name,
            "receiverAddress": self.receiver_address,
            "tenorInstalment": self.tenor_instalment,
            "fullName": self.full_name,
            "idCardNo": self.id_card_no,
            "birthDate": self.birth_date,
            "address": self.address,
            "handphone": self.handphone,
            "phone": self.phone,
            "office_name": self.office_name,
            "office_phone": self.office_phone,
            "sibling_name": self.sibling_name,
            "sibling_phone": self.sibling_phone
        }

    @property
    def validation(self):
        if not self.id_card_no.isdigit():
            # return "Input error: ID card number is not a number"
            return "Error"

        if not self.handphone.isdigit():
            # return "Input error: Handphone is not a number"
            return "Error"

        if not self.phone.isdigit():
            # return "Input error: Phone is not a number"
            return "Error"

        if not self.sibling_phone.isdigit():
            # return "Input error: Sibling phone is not a number"
            return "Error"

        return "Success"




