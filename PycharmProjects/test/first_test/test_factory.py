import unittest
from factory import Factory


class TestFactory(unittest.TestCase):

    def test_factory_can_add_item_to_conveyor_belt(self):
        factory = Factory()
        factory.add_to_conveyor_belt(55)
        factory.add_to_conveyor_belt(55)
        factory.add_to_conveyor_belt(55)
        self.assertEqual(factory.conveyor_belt.__len__(), 3)

    def test_add_random_items_to_conveyor_belt(self):
        factory = Factory()
        factory.add_random_items_to_conveyor_belt()
        self.assertEqual(factory.conveyor_belt.__len__(), 10)

    def test_item_placed_in_holding_area(self):
        factory = Factory()
        factory.add_random_items_to_conveyor_belt()
        factory.check_object_at_position_zero()
        self.assertEqual(factory.holding_area.__len__(), 1)
