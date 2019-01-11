"""
Exceptions
==========

Specialized error types raised from AkuLaku.
"""
__all__ = ['KreditPlusError', ]


class KreditPlusError(Exception):
    """ Raised when the KreditPlus validation error
    """
    def __eq__(self, other):
        if type(other) != type(self):
            return False
        elif other.args == self.args:
            return True
        return False
