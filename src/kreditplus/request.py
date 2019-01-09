import logging

from kreditplus.exceptions import KreditPlusError
log = logging.getLogger('kreditplus')


class KreditPlusRequest:

    def create_order(self, order_request):
        """ Create a new order to the KreditPlus
        """
        data = order_request.serialize()

        return data;

