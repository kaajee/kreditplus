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
                 order_number,
                 order_price,
                 month_installment,
                 name,
                 ktp_number,
                 birthdate,
                 address,
                 mobile_phone,
                 phone,
                 office_name,
                 office_phone,
                 sibling_name,
                 sibling_phone):
        self.order_number = order_number
        self.order_price = order_price
        self.month_installment = month_installment
        self.name = name
        self.ktp_number = ktp_number
        self.birthdate = birthdate
        self.address = address
        self.mobile_phone = mobile_phone
        self.phone = phone
        self.office_name = office_name
        self.office_phone = office_phone
        self.sibling_name = sibling_name
        self.sibling_phone = sibling_phone

    def serialize(self):

        return {
            "order_number": self.order_number,
            "order_price": self.order_price,
            "month_installment": self.month_installment,
            "name": self.name,
            "ktp_number": self.ktp_number,
            "birthdate": self.birthdate,
            "address": self.address,
            "mobile_phone": self.mobile_phone,
            "phone": self.phone,
            "office_name": self.office_name,
            "office_phone": self.office_phone,
            "sibling_name": self.sibling_name,
            "sibling_phone": self.sibling_phone,
        }
