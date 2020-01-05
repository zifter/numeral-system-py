"""
All exceptions which can be thrown by this module during work.
"""


class NumericSystemException(BaseException):
    """
    Base for all exceptions from this module.
    """


class WrongArgumentTypeError(NumericSystemException):
    """
    Occurs when argument type is wrong
    """


class WrongArgumentValueError(NumericSystemException):
    """
    Occurs when argument value is wrong
    """


class NumberOutOfRangeError(NumericSystemException):
    """
    Occurs when number can't be converted to necessary numeric system
    """


class IncorrectNumberRepresentationError(NumericSystemException):
    """
    Occurs when representation of number is incorrect according to numeric system
    """
