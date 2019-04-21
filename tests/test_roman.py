from unittest import TestCase

from parameterized import parameterized

from numeral_system import roman, exceptions


class RomanTestCase(TestCase):
    @parameterized.expand([
        ('I', 1),
        ('II', 2),
        ('III', 3),
        ('IV', 4),
        ('V', 5),
        ('VI', 6),
        ('VII', 7),
        ('VIII', 8),
        ('IX', 9),
        ('X', 10),
        ('XI', 11),
        ('XII', 12),
        ('XIII', 13),
        ('XIV', 14),
        ('XV', 15),
        ('XVI', 16),
        ('XVII', 17),
        ('XVIII', 18),
        ('XIX', 19),
        ('XX', 20),
        ('XXI', 21),
        ('CCLXXXIII', 283),
        ('MCMLXXXVIII', 1988),
    ])
    def tests_check_base_numbers_to_roman(self, expected, number):
        result = roman.encode(number)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ('negative_1', -1),
        ('negative_100', -100),
        ('zero', 0),
        ('greater_4000', 4000),
        ('greater_21454', 21454),
    ])
    def tests_out_of_range_roman_numbers(self, _, number):
        with self.assertRaises(exceptions.NumberOutOfRangeError):
            roman.encode(number)

    @parameterized.expand([
        ('string', 'str_value'),
        ('float', 1.),
        ('list', []),
    ])
    def tests_wrong_type_of_number(self, _, number):
        with self.assertRaises(exceptions.WrongTypeError):
            roman.encode(number)

    def tests_check_all_digits(self):
        for i in range(1, 4000):
            roman_number = roman.encode(i)
            self.assertEqual(roman.decode(roman_number), i)

    @parameterized.expand([
        ('string', 1),
        ('float', 1.),
        ('list', []),
    ])
    def tests_wrong_type_roman_number(self, _, number):
        with self.assertRaises(exceptions.WrongTypeError):
            roman.decode(number)

    @parameterized.expand([
        ('0',),
        ('VIIII',),
        ('list',),
        ('XMX',),
    ])
    def tests_wrong_representation_roman_number(self, number):
        with self.assertRaises(exceptions.IncorrectNumberRepresentationError):
            roman.decode(number)

    def tests_check_valid_roman_number(self):
        for i in range(1, 4000):
            roman_number = roman.encode(i)
            self.assertTrue(roman.is_valid(roman_number))

    @parameterized.expand([
        ('IIII',),
        ('VIIII',),
        ('list',),
        ('XMX',),
    ])
    def tests_check_invalid_roman_number(self, number):
        self.assertFalse(roman.is_valid(number))
