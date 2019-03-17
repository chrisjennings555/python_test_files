import random
from worker import Worker


class Factory:

    def __init__(self):
        self.conveyor_belt = []
        self.worker = Worker
        self.holding_area = []

    def add_to_conveyor_belt(self, item):
        self.conveyor_belt.append(item)

    def add_random_items_to_conveyor_belt(self):
        for i in range(0, 10):
            x = random.randint(0, 2)
            if x == 1:
                self.conveyor_belt.append("wotsit")
            elif x == 2:
                self.conveyor_belt.append("widget")
            elif x == 0:
                self.conveyor_belt.append("empty")

        print(self.conveyor_belt)

    def add_item_to_holding_area(self, item):
        self.holding_area.append(item)

    def check_object_at_position_zero(self):
        if self.conveyor_belt[0] == "wotsit":
            self.add_item_to_holding_area(self.conveyor_belt.pop(0))
        elif self.conveyor_belt[0] == 'widget':
            self.add_item_to_holding_area(self.conveyor_belt.pop(0))
        elif self.conveyor_belt[0] == "empty":
            pass

    def add_item_to_worker_basket(self):
        if self.holding_area.__len__() == 1:
            new_item = self.holding_area.pop()
            self.worker.add_item_to_basket(new_item)
        else:
            pass

    def run_conveyor_belt(self):
        self.add_random_items_to_conveyor_belt()

        for i in range(1, self.conveyor_belt.__len__()):
            self.check_object_at_position_zero()
            self.add_item_to_worker_basket()
            print(self.worker)

