from unittest import TestCase
from GUI.map import get_text


class Test(TestCase):
    def test_level_greater_than_current_level(self):
        room_description = [2, 'Street', 'Nothing']
        current_level = 1
        expected_output = ''
        actual_output = get_text(room_description, current_level)
        self.assertEqual(actual_output, expected_output)

    def test_level_equal_current_level_has_item_to_pickup(self):
        room_description = [1, 'Kitchen', 'Hot Water']
        current_level = 1
        actual_output = get_text(room_description, current_level)
        expected_output = 'Hot Water'
        self.assertEqual(actual_output, expected_output)

    def test_level_equal_current_level_door(self):
        room_description = [3, 'Street', 'Door']
        current_level = 3
        expected_output = 'Door'
        actual_output = get_text(room_description, current_level)
        self.assertEqual(actual_output, expected_output)

    def test_level_equal_current_level_nothing(self):
        room_description = [2, 'Grocery Store', 'Nothing']
        current_level = 2
        expected_output = 'Grocery Store'
        actual_output = get_text(room_description, current_level)
        self.assertEqual(actual_output, expected_output)

    def test_level_equal_current_level_chocolate(self):
        room_description = [2, 'Street', 'Chocolate']
        current_level = 2
        expected_output = 'Chocolate'
        actual_output = get_text(room_description, current_level)
        self.assertEqual(actual_output, expected_output)

    def test_level_less_than_current_level_has_item_to_pickup(self):
        room_description = [1, 'Kitchen', 'Hot Water']
        current_level = 2
        actual_output = get_text(room_description, current_level)
        expected_output = 'Hot Water'
        self.assertEqual(actual_output, expected_output)

    def test_level_less_than_current_level_door(self):
        room_description = [2, 'Street', 'Door']
        current_level = 3
        expected_output = 'Door'
        actual_output = get_text(room_description, current_level)
        self.assertEqual(actual_output, expected_output)

    def test_level_less_than_current_level_nothing(self):
        room_description = [2, 'Grocery Store', 'Nothing']
        current_level = 3
        expected_output = 'Grocery Store'
        actual_output = get_text(room_description, current_level)
        self.assertEqual(actual_output, expected_output)

    def test_level_less_than_current_level_chocolate(self):
        room_description = [2, 'Street', 'Chocolate']
        current_level = 3
        expected_output = 'Chocolate'
        actual_output = get_text(room_description, current_level)
        self.assertEqual(actual_output, expected_output)

    def test_at_destination(self):
        room_description = [4, 'Destination', 'Joey and Hsin']
        current_level = 4
        expected_output = 'Joey and Hsin'
        actual_output = get_text(room_description, current_level)
        self.assertEqual(actual_output, expected_output)

    def test_game_just_begin_at_origin(self):
        room_description = [1, 'Kitchen', 'Origin']
        current_level = 1
        expected_output = 'Origin'
        actual_output = get_text(room_description, current_level)
        self.assertEqual(actual_output, expected_output)

    def test_higher_level_at_origin(self):
        room_description = [1, 'Kitchen', 'Origin']
        current_level = 4
        expected_output = 'Origin'
        actual_output = get_text(room_description, current_level)
        self.assertEqual(actual_output, expected_output)