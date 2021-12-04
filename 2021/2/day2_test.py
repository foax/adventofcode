from unittest import TestCase
import day2
import fileinput

test_input = day2.load_input(fileinput.input(
    'test_input'), lambda x: x.rstrip().split(' '))


class TestSubClass(TestCase):
    def setUp(self):
        self.sub = day2.Sub('test')

    def test_sub_forward(self):
        cur_pos = self.sub.position
        fwd_amount = 1
        self.sub.forward(fwd_amount)
        self.assertEqual(self.sub.position, cur_pos + fwd_amount)

    def test_sub_down(self):
        cur_depth = self.sub.depth
        down_amount = 1
        self.sub.down(down_amount)
        self.assertEqual(self.sub.depth, cur_depth + down_amount)

    def test_sub_up(self):
        cur_depth = self.sub.depth
        up_amount = 1
        self.sub.up(up_amount)
        self.assertEqual(self.sub.depth, cur_depth - up_amount)

    def test_do_commands(self):
        self.sub.do_commands(test_input)
        self.assertEqual(self.sub.position, 15)
        self.assertEqual(self.sub.depth, 10)


class TestSubCollinsClass(TestCase):
    def setUp(self):
        self.sub = day2.Collins('test')

    def test_sub_down(self):
        cur_aim = self.sub.aim
        down_amount = 3
        self.sub.down(down_amount)
        self.assertEqual(self.sub.aim, cur_aim + down_amount)

    def test_sub_up(self):
        cur_aim = self.sub.aim
        up_amount = 3
        self.sub.up(up_amount)
        self.assertEqual(self.sub.aim, cur_aim - up_amount)

    def test_sub_forward(self):
        cur_pos = self.sub.position
        cur_depth = self.sub.depth
        forward_amount = 3
        aim_amount = 2
        self.sub.down(aim_amount)
        self.sub.forward(forward_amount)
        self.assertEqual(self.sub.position, cur_pos + forward_amount)
        self.assertEqual(self.sub.depth, cur_depth +
                         aim_amount * forward_amount)

    def test_do_commands(self):
        self.sub.do_commands(test_input)
        self.assertEqual(self.sub.position, 15)
        self.assertEqual(self.sub.depth, 60)
