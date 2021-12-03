from unittest import TestCase
import day3
import fileinput

test_input = day3.load_input(fileinput.input(
    'test_input'), lambda x: int(x.rstrip(), 2))


class TestFunctions(TestCase):

    def test_bit_count(self):
        count = day3.bit_count(test_input)
        expected_count = {1: 5, 2: 7, 4: 8,  8: 5, 16: 7}
        self.assertEqual(count, expected_count)

    def test_bit_count_subtract(self):
        count = {1: 5, 2: 7, 4: 8, 8: 5, 16: 7}
        expected_count = {1: 4, 2: 7, 4: 7, 8: 5, 16: 6}
        # int('10101', 2) = 21
        day3.bit_count_subtract(count, 21)
        self.assertEqual(count, expected_count)

    def test_find_gamma(self):
        self.assertEqual(day3.find_gamma(test_input), 22)

    def test_find_rating(self):
        self.assertEqual(day3.find_rating(test_input), 23)
        self.assertEqual(day3.find_rating(test_input, invert=True), 10)
