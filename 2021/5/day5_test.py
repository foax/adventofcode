from unittest import TestCase
import day5
import textwrap

lines = day5.load_lines('test_input')


class TestFunctions(TestCase):

    def test_load_lines(self):
        lines = day5.load_lines('test_input')
        expected_lines = [((0, 9), (5, 9)), ((8, 0), (0, 8)), ((9, 4), (3, 4)), ((2, 2), (2, 1)), ((7, 0), (7, 4)), ((
            6, 4), (2, 0)), ((0, 9), (2, 9)), ((3, 4), (1, 4)), ((0, 0), (8, 8)), ((5, 5), (8, 2))]
        self.assertEqual(lines, expected_lines)

    def test_find_extents(self):
        max_x, max_y = day5.find_extents(lines)
        self.assertEqual(max_x, 9)
        self.assertEqual(max_y, 9)

    def test_empty_space(self):
        empty_space = day5.empty_space(lines)
        expected_space = [[0] * 10] * 10
        self.assertEqual(empty_space, expected_space)

    def test_mark_lines(self):
        expected_output = '''\
.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
'''
        space = day5.empty_space(lines)
        day5.mark_lines(lines, space)
        self.assertEqual(day5.space_as_str(space), expected_output)

    def test_mark_lines_with_diagonals(self):
        expected_output = '''\
1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
'''
        space = day5.empty_space(lines)
        day5.mark_lines(lines, space, check_diagonals=True)
        self.assertEqual(day5.space_as_str(space), expected_output)
