"""
Models
======
Represent data that is sent to the the KreditPlus.
"""

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
                 email):
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
        self.email = email

    @property
    def content(self):
        """ Generates a stringified verision of this object not for API consumption, but for generating signatures.

        :rtype: str
        """
        required_attributes = [
            'ref_number', 'total_price', 'product_name', 'receiver_name', 'receiver_address', 'tenor_instalment',
            'full_name', 'id_card_no', 'birth_date', 'address', 'handphone', 'email',
        ]
        return ''.join([getattr(self, attr) for attr in required_attributes])

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
            "email": self.email,
        }

