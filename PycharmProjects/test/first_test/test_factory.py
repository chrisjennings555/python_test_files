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

    def test_add_random_items_to_conveyor_belt(self):
        factory = Factory()
        factory.add_random_items_to_conveyor_belt()
        self.assertEqual(factory.conveyor_belt.__len__(), 10)

    def test_item_placed_in_holding_area(self):
        factory = Factory()
        factory.add_random_items_to_conveyor_belt()
        factory.move_item_at_position_zero_to_holding_area()
        self.assertEqual(factory.holding_area.__len__(), 1)

    def test_items_moved_from_belt_to_holding_area_and_reverse(self):
        factory = Factory()
        factory.add_random_items_to_conveyor_belt()
        factory.move_item_at_position_zero_to_holding_area()
        factory.worker_assessment_of_holding_area()
        self.assertEqual(factory.conveyor_belt.__len__(), 10)

    def test_item_sent_to_recycling(self):
        factory = Factory()
        factory.add_random_items_to_conveyor_belt()
        factory.move_item_at_position_zero_to_holding_area()
        factory.worker_assessment_of_holding_area()
        factory.send_to_recycling()
        print("after running once", factory.conveyor_belt)
        print("worker basket PR", factory.worker.basket)
        print("recycling PR", factory.recycling_bin)
        self.assertEqual(factory.recycling_bin.__len__(), 1)
        self.assertEqual(factory.conveyor_belt.__len__(), 9)

    def test_factory_can_run(self):
        factory = Factory()
        factory.add_random_items_to_conveyor_belt()
        print("initial conveyor order", factory.conveyor_belt)
        factory.run_factory()
        print("recycling after run", factory.recycling_bin)
        self.assertEqual(factory.conveyor_belt.__len__(), 0)
