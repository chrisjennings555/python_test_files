import unittest
from factory import Factory
from worker import Worker


class TestFactory(unittest.TestCase):

    def test_factory_can_add_item_to_conveyor_belt(self):
        factory = Factory()
        factory.add_to_conveyor_belt(55)
        factory.add_to_conveyor_belt(55)
        factory.add_to_conveyor_belt(55)
        self.assertEqual(factory.conveyor_belt.__len__(), 3)

    # def test_add_random_items_to_conveyor_belt(self):
    #     factory = Factory()
    #     factory.add_random_items_to_conveyor_belt()
    #     self.assertEqual(factory.conveyor_belt.__len__(), 10)


