"""
Tests for positional numeral system
"""
from random import randint
from unittest import TestCase

from numeral_system import exceptions, positional
from parameterized import parameterized
from six import moves


class PositionalTestCase(TestCase):
    """
    Positional numeral system checks
    """

    @parameterized.expand(
        [
            # name, number, base, expected
            (42, 10, "42"),
            (2, 2, "10"),
            (15, 2, "1111"),
            (2019, 16, "7E3"),
            (-213, 16, "-D5"),
            # TODO more negative and more examples
        ]
    )
    def test_check_base_numbers_to_positional(self, number, base, expected):
        """
        Manual check if converting is correction
        """
        result = positional.encode(number, base)
        self.assertEqual(result, expected)

    @parameterized.expand(
        [
            (randint(-9999, 9999), base)
            for _ in moves.range(5)
            for base in moves.range(2, positional.max_base())
        ]
    )
    def test_check_all_default_bases_positional(self, number, base):
        """
        Auto check of encoding and decoding
        """
        converted = positional.encode(number, base)
        self.assertEqual(positional.decode(converted, base), number)

    @parameterized.expand(
        [(4112, 5, 532), ("4111", 5, 531), (1129, 10, 1129), ("1129", 10, 1129),]
    )
    def test_decode_numbers(self, number, base, expected):
        """
        Auto check of encoding and decoding
        """
        self.assertEqual(positional.decode(number, base), expected)

    @parameterized.expand(
        [(0,), (-1,), (1000,),]
    )
    def test_check_incorrect_base(self, base):
        """
        Check converting with wrong base
        """
        with self.assertRaises(exceptions.WrongArgumentValueError):
            positional.encode(42, base)

    @parameterized.expand(
        [(1123, 11), ((1, 2, 3), 10), ((1, 2, 3), 5),]
    )
    def test_check_wrong_argument_type(self, number, base):
        """
        Check converting with wrong base
        """
        with self.assertRaises(exceptions.WrongArgumentTypeError):
            positional.decode(number, base)

    @parameterized.expand(
        [("duplicated", ("1", "2", "3", "3"),),]
    )
    def test_check_digits_with_wrong_alphabet(self, _, alpha):
        """
        Alphabet is not correct
        """
        with self.assertRaises(exceptions.WrongArgumentValueError):
            positional.encode(42, 10, alphabet=alpha)

    @parameterized.expand(
        [
            (0, 4, "Z"),
            (3, 4, "#"),
            (987, 10, "(E&"),
            (789, 10, "&E("),
            (9876543210, 10, "(E&S%F#T!Z"),
            (-9876543210, 10, "@(E&S%F#T!Z"),
        ]
    )
    def test_check_digits_with_custom_alphabet_and_sign(self, number, base, expected):
        """
        Checks with custom alphabet and sign
        """
        alphabet = ("Z", "!", "T", "#", "F", "%", "S", "&", "E", "(", "0")

        converted = positional.encode(number, base, alphabet=alphabet, sign_literal="@")
        self.assertEqual(converted, expected)
        self.assertEqual(
            positional.decode(converted, base, alphabet=alphabet, sign_literal="@"),
            number,
        )

    @parameterized.expand(
        [(0, "0"), (5, "101"), (10, "1010"),]
    )
    def test_binary_helpers(self, number, expected):
        """
        Check binary help functions
        """
        self.assertEqual(positional.from_binary(expected), number)
        self.assertEqual(positional.to_binary(number), expected)
        self.assertEqual(positional.to_binary(str(number)), expected)

    @parameterized.expand(
        [(0, "0"), (5, "5"), (10, "12"), (17, "21"), (89, "131"),]
    )
    def test_octal_helpers(self, number, expected):
        """
        Check octal help functions
        """
        self.assertEqual(positional.from_octal(expected), number)
        self.assertEqual(positional.to_octal(number), expected)
        self.assertEqual(positional.to_octal(str(number)), expected)

    @parameterized.expand(
        [(0, "0"), (5, "5"), (10, "A"), (89, "59"), (213, "D5"),]
    )
    def test_hex_helpers(self, number, expected):
        """
        Check hex help functions
        """
        self.assertEqual(positional.from_hex(expected), number)
        self.assertEqual(positional.to_hex(number), expected)

    @parameterized.expand(
        [(2, "0"), (6, "5"), (16, "A"), (12, "59"), (16, "D5"),]
    )
    def test_valid_numbers(self, base, number):
        """
        Check valid numbers
        """
        self.assertTrue(positional.is_valid(number, base))

    @parameterized.expand(
        [(2, ""), (4, "5"), (10, "A"), (11, "D5"),]
    )
    def test_invalid_numbers(self, base, number):
        """
        Check invalid numbers
        """
        self.assertFalse(positional.is_valid(number, base))

    def test_wrong_alphabet(self):
        """
        Check negative case with invalid alphabet
        """
        with self.assertRaises(exceptions.WrongArgumentValueError):
            positional.decode(4, 2, alphabet=tuple("12344"))

    def test_wrong_argument_for_encoding(self):
        """
        Check negative case with wrong type encoding number
        """
        with self.assertRaises(exceptions.WrongArgumentTypeError):
            positional.encode(4.5, 10)
