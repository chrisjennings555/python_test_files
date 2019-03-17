import unittest
from worker import Worker


class TestWorker(unittest.TestCase):

    def test_item_can_be_added_to_worker_basket(self):
        worker = Worker()
        worker.add_item_to_basket("widget")
        self.assertEqual(worker.basket.__len__(), 1)

    def test_worker_can_accurately_check_holding_area(self):
        worker = Worker()
        worker.check_item_in_holding_area("wotsit")
        worker.check_item_in_holding_area("empty")
        worker.check_item_in_holding_area("empty")
        worker.check_item_in_holding_area("wotsit")
        worker.check_item_in_holding_area("widget")
        worker.check_item_in_holding_area("widget")
        self.assertEqual(worker.basket.__len__(), 2)

    def test_worker_can_build_thingamajig(self):
        worker = Worker()
        worker.check_item_in_holding_area("wotsit")
        worker.check_item_in_holding_area("empty")
        worker.check_item_in_holding_area("empty")
        worker.check_item_in_holding_area("wotsit")
        worker.check_item_in_holding_area("widget")
        worker.check_item_in_holding_area("widget")
        worker.build_thingamajig()
        self.assertEqual(worker.basket.__contains__("thingamajig"), True)

    def test_worker_can_send_thingamajig_to_holding_area(self):
        worker = Worker()
        worker.check_item_in_holding_area("wotsit")
        worker.check_item_in_holding_area("empty")
        worker.check_item_in_holding_area("empty")
        worker.check_item_in_holding_area("wotsit")
        worker.check_item_in_holding_area("widget")
        worker.check_item_in_holding_area("widget")
        worker.build_thingamajig()
        worker.send_thingamajig_to_holding_area()
        self.assertEqual(worker.basket.__len__(), 0)
