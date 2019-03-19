import unittest
from worker import Worker


class TestWorker(unittest.TestCase):

    def test_item_can_be_added_to_worker_basket(self):
        worker = Worker(1)
        worker.add_item_to_basket("widget")
        self.assertEqual(worker.basket.__len__(), 1)

    def test_worker_can_accurately_check_holding_area(self):
        worker = Worker(1)
        worker.does_worker_need_item("wotsit")
        worker.does_worker_need_item("empty")
        worker.does_worker_need_item("empty")
        worker.does_worker_need_item("wotsit")
        worker.does_worker_need_item("widget")
        worker.does_worker_need_item("widget")
        self.assertEqual(worker.basket.__len__(), 2)

    def test_items_ready_for_build(self):
        worker = Worker(1)
        worker.does_worker_need_item("wotsit")
        worker.does_worker_need_item("widget")
        self.assertEqual(worker.check_items_ready_to_build_thingamajig(), True)



