"""
All exceptions which can be thrown by this module during work.
"""


class NumericSystemException(BaseException):
    """
    Base for all exceptions from this module.
    """
    pass


class WrongTypeError(NumericSystemException):
    """
    Occuries when argument type is wrong
    """
    pass


class NumberOutOfRangeError(NumericSystemException):
    """
    Occuries when number can't be converted to necessary numeric system
    """
    pass


class IncorrectNumberRepresentationError(NumericSystemException):
    """
    Occuries representation of number is incorrect accoring to numeric system
    """
    pass
