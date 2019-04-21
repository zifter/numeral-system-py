"""
This package contains functions for converting integer into roman and backward
"""
import re

from .exceptions import WrongTypeError, NumberOutOfRangeError, IncorrectNumberRepresentationError


# order is important
_ALPHA = (
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
)


def is_valid(number):
    """
    Check if number is roman

    :param number: string to check
    :type number: str

    :return: True or False
    :rtype: bool
    """
    return re.match(r'^(M{0,3})(D?C{0,3}|C[DM])(L?X{0,3}|X[LC])(V?I{0,3}|I[VX])$', number)


def encode(number):
    """
    Convert integer from 1 to 3999 to roman number

    :param number: integer number
    :type number: int

    :return: roman number as string
    :rtype: str
    """
    if not isinstance(number, int):
        raise WrongTypeError('Integer number is expected, but {} was given'.format(type(number)))

    if number < 0:
        raise NumberOutOfRangeError('Negative values are not allowed in roman')

    if number == 0:
        raise NumberOutOfRangeError('Zero values is not allowed in roman')

    if number > 3999:
        raise NumberOutOfRangeError(r'Number is too big - roman numbers can\'t be greater or equal 4000')

    # TODO Binary search
    result = ''
    for num, view in _ALPHA:
        while number >= num:
            number -= num
            result += view

    return result


def decode(number):
    """
    Convert string in roman representation to integer number

    :param number: roman number as string
    :type number: str

    :return: integer number
    :rtype: int
    """
    if not isinstance(number, str):
        raise WrongTypeError('Wrong type of roman number: expected string but {} was given'.format(type(number)))

    if not is_valid(number):
        raise IncorrectNumberRepresentationError('It\'s not a roman string {}'.format(number))

    result = 0
    remain = number
    for num, view in _ALPHA:
        while True:
            if remain.startswith(view):
                roman_view_len = len(view)
                _, remain = remain[:roman_view_len], remain[roman_view_len:]
                result += num
            else:
                break

    assert not remain

    return result
