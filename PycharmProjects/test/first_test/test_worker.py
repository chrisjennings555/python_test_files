import unittest
from worker import Worker


class TestWorker(unittest.TestCase):

    def test_item_can_be_added_to_worker_basket(self):
        worker = Worker()
        worker.add_item_to_basket("widget")
        self.assertEqual(worker.basket.__len__(), 1)

    def test_worker_can_reject_duplicates(self):
        worker = Worker()
        item = "widget"
        worker.does_worker_need_item(item)
        worker.does_worker_need_item(item)
        self.assertEqual(worker.basket.__len__(), 1)

    def test_worker_can_reject_empty(self):
        worker = Worker()
        item = "empty"
        worker.does_worker_need_item(item)
        self.assertEqual(worker.basket.__len__(), 0)

    def test_worker_can_reject_thingamajig(self):
        worker = Worker()
        item = "thingamajig"
        worker.does_worker_need_item(item)
        self.assertEqual(worker.basket.__len__(), 0)

    def test_worker_can_accept_multiple_items(self):
        worker = Worker()
        item1 = "wotsit"
        item2 = "widget"
        worker.does_worker_need_item(item1)
        worker.does_worker_need_item(item2)
        self.assertEqual(worker.basket.__len__(), 2)

    def test_worker_can_build_thingamajig(self):
        worker = Worker()
        item1 = "wotsit"
        item2 = "widget"
        worker.does_worker_need_item(item1)
        worker.does_worker_need_item(item2)
        worker.check_items_ready_to_build_thingamajig()
        self.assertEqual(worker.basket.__contains__("thingamajig"), True)
        # also assert that basket has been cleared and only 1 item exists
        self.assertEqual(worker.basket.__len__(), 1)










