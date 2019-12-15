"""
Allows convert numbers in different positional numeral system.
The most used are binary, octal, decimal and hexadecimal
"""
import numbers
from itertools import groupby

try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache


from .exceptions import WrongArgumentValueError, WrongArgumentTypeError


_DEFAULT_ALPHABET = tuple('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
_DEFAULT_SIGN = '-'


def max_base(alphabet=_DEFAULT_ALPHABET):
    """
    Get max base for given alphabet

    :param alphabet:
    :type alphabet: tuple

    :return:
    :rtype: int
    """
    return len(alphabet)


def _sign(number):
    """
    Get sign of the given number

    :param number:
    :type number: int

    :return: -1, 0, 1
    :rtype: int
    """
    if number > 0:
        return 1

    if number < 0:
        return -1

    return 0


@lru_cache(maxsize=32)
def _map_digit_to_int(alphabet):
    """
    Return mapped literal representation to digit

    :param alphabet: alphabet of numeric system
    :type alphabet: tuple

    :return: {'0': 0, '1': 1, ...}
    :rtype: dict
    """
    assert isinstance(alphabet, tuple)

    mapping = {digit: i for i, digit in enumerate(alphabet)}

    if len(mapping) != len(alphabet):
        grouped_data = [digit for digit, group in groupby(sorted(alphabet)) if len(list(group)) > 1]
        raise WrongArgumentValueError('Duplicated symbols in alphabet {}'.format(grouped_data))

    return mapping


def _raise_if_alphabet_is_invalid(base, alphabet):
    """
    Check given alphabet and base

    :param base:
    :type base:

    :param alphabet: alphabet of numeric system
    :type alphabet: tuple
    """
    if base <= 1 or base > max_base(alphabet=alphabet):
        raise WrongArgumentValueError('Base should be in range [{}, {}]. Passed base is {}'
                                      .format(1, max_base(alphabet=alphabet), base))


def _split_digits(number, sign_literal):
    """
    Split given number per literal and sign

    :param number:
    :type number: int | str

    :param base:
    :type base: int

    :param sign_literal:
    :type sign_literal: str

    :return: sign, digits
    :rtype: int, list
    """
    digits = list(str(number))
    sign = 1
    if digits[0] == sign_literal:
        sign = -1
        digits = digits[1:]

    return sign, digits


def is_valid(number, base, alphabet=_DEFAULT_ALPHABET, sign_literal=_DEFAULT_SIGN):
    """
    Check if given number is valid in given base and alphabet

    :param number: given number to check
    :type number: int | str

    :param base: base of given number
    :type base: int | str for less base

    :param alphabet: alphabet of numeric system
    :type alphabet: tuple

    :param sign_literal:
    :type sign_literal: str

    :return: True if given number is valid in positional numeral system with base
    :rtype: bool
    """
    _raise_if_alphabet_is_invalid(base, alphabet)

    if not number:
        return False

    _, digits = _split_digits(number, sign_literal)
    for digit in digits:
        if digit not in alphabet[0:base]:
            return False

    return True


def encode(number, base, alphabet=_DEFAULT_ALPHABET, sign_literal=_DEFAULT_SIGN):
    """
    Convert integer number to number with given base and alphabet

    :param number: given number to convert
    :type number: int | str

    :param base: base of given number
    :param base: int | str for less base

    :param alphabet: alphabet of numeric system
    :type alphabet: tuple

    :param sign_literal:
    :type sign_literal: str

    :return: converted number
    :rtype: str
    """
    _raise_if_alphabet_is_invalid(base, alphabet)

    if base <= 10 and isinstance(number, str):
        number = int(number)

    if not isinstance(number, numbers.Integral):
        raise WrongArgumentTypeError('Number to encode should be integer, not {}'.format(type(number)))

    number = int(number)
    number_sign = _sign(number)
    number = number_sign * number

    pos = []
    while number >= base:
        mod = number % base
        pos.append(alphabet[mod])
        number = number // base

    pos.append(alphabet[number])

    result = ''
    if number_sign == -1:
        result = sign_literal

    return result + ''.join(reversed(pos))


def decode(number, base, alphabet=_DEFAULT_ALPHABET, sign_literal=_DEFAULT_SIGN):
    """
    Convert number from given base and alphabet to integer

    :param number: given number to convert
    :type number: int | str

    :param base: base of given number
    :type base: int | str for less base

    :param alphabet: alphabet of numeric system
    :type alphabet: tuple

    :param sign_literal:
    :type sign_literal: str

    :return: converted number
    :rtype: str
    """
    _raise_if_alphabet_is_invalid(base, alphabet)

    if base > 10 and not isinstance(number, str):
        raise WrongArgumentTypeError('Number to encode with base greater 10 should be string')

    if base <= 10 and not isinstance(number, (int, str)):
        raise WrongArgumentTypeError('Number to encode with base less or equal 10 should be string or integer')

    sign, digits = _split_digits(number, sign_literal)
    mapping = _map_digit_to_int(alphabet)
    as_literals = reversed(digits)
    return sign * sum((mapping[digit] * pow(base, index) for index, digit in enumerate(as_literals)))


########
# Binary
def to_binary(number):
    """
    To binary number representation from integer

    :param number:
    :type number: int | str

    :return:
    :rtype: str
    """
    return encode(number, 2)


def from_binary(number):
    """
    To hexadecimal number representation from integer

    :param number:
    :type number: int | str

    :return:
    :rtype: str
    """
    return decode(number, 2)


########
# Octal
def to_octal(number):
    """
    To hexadecimal number representation from integer

    :param number:
    :type number: int | str

    :return:
    :rtype: str
    """
    return encode(number, 8)


def from_octal(number):
    """
    From hexadecimal number representation to integer

    :param number:
    :type number: int | str

    :return:
    :rtype: str
    """
    return decode(number, 8)


########
# Hexadecimal
def to_hex(number):
    """
    To hexadecimal number representation from integer

    :param number:
    :type number: str

    :return:
    :rtype: str
    """
    return encode(number, 16)


def from_hex(number):
    """
    From hexadecimal number representation to integer

    :param number:
    :type number: str

    :return:
    :rtype: str
    """
    return decode(number, 16)
