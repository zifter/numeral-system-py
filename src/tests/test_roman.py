"""
Tests for roman numeral system
"""
from unittest import TestCase

import six
from numeral_system import exceptions, roman
from parameterized import parameterized


class RomanTestCase(TestCase):
    """
    Roman numeral system checks
    """

    @parameterized.expand(
        [
            ("I", 1),
            ("II", 2),
            ("III", 3),
            ("IV", 4),
            ("V", 5),
            ("VI", 6),
            ("VII", 7),
            ("VIII", 8),
            ("IX", 9),
            ("X", 10),
            ("XI", 11),
            ("XII", 12),
            ("XIII", 13),
            ("XIV", 14),
            ("XV", 15),
            ("XVI", 16),
            ("XVII", 17),
            ("XVIII", 18),
            ("XIX", 19),
            ("XX", 20),
            ("XXI", 21),
            ("CCLXXXIII", 283),
            ("MCMLXXXVIII", 1988),
        ]
    )
    def test_check_base_numbers_to_roman(self, expected, number):
        """
        Manual check if converting is correction
        """
        result = roman.encode(number)
        self.assertEqual(result, expected)

    @parameterized.expand(
        [
            ("negative_1", -1),
            ("negative_100", -100),
            ("zero", 0),
            ("greater_4000", 4000),
            ("greater_21454", 21454),
        ]
    )
    def test_out_of_range_roman_numbers(self, _, number):
        """
        Check wrong number converting
        """
        with self.assertRaises(exceptions.NumberOutOfRangeError):
            roman.encode(number)

    @parameterized.expand(
        [("string", "str_value"), ("float", 1.0), ("list", []),]
    )
    def test_wrong_type_of_number(self, _, number):
        """
        Check wrong type of passed argument
        """
        with self.assertRaises(exceptions.WrongArgumentTypeError):
            roman.encode(number)

    def test_check_all_digits(self):
        """
        Auto check of all converting
        """
        for i in six.moves.range(1, 4000):
            roman_number = roman.encode(i)
            self.assertEqual(roman.decode(roman_number), i)

    @parameterized.expand(
        [("string", 1), ("float", 1.0), ("list", []),]
    )
    def test_wrong_type_roman_number(self, _, number):
        """
        Check wring type of passed argument
        """
        with self.assertRaises(exceptions.WrongArgumentTypeError):
            roman.decode(number)

    @parameterized.expand(
        [("0",), ("VIIII",), ("list",), ("XMX",),]
    )
    def test_wrong_representation_roman_number(self, number):
        """
        Check wrong roman numbers
        """
        with self.assertRaises(exceptions.IncorrectNumberRepresentationError):
            roman.decode(number)

    def test_check_valid_roman_number(self):
        """
        Check is_valid functions for valid roman numbers
        """
        for i in six.moves.range(1, 4000):
            roman_number = roman.encode(i)
            self.assertTrue(roman.is_valid(roman_number))

    @parameterized.expand(
        [("IIII",), ("VIIII",), ("list",), ("XMX",),]
    )
    def test_check_invalid_roman_number(self, number):
        """
        Check is_valid functions for invalid roman numbers
        """
        self.assertFalse(roman.is_valid(number))
