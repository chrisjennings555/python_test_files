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
                self.add_to_conveyor_belt("wotsit")
            elif x == 2:
                self.add_to_conveyor_belt("widget")
            elif x == 0:
                self.add_to_conveyor_belt("empty")

        print(self.conveyor_belt)

    def add_item_to_holding_area(self, item):
        self.holding_area.append(item)

    def check_object_at_position_zero(self):
        if self.conveyor_belt[0] == "wotsit":
            self.add_item_to_holding_area(self.conveyor_belt.pop(0))
            self.conveyor_belt.insert(0, "empty")
        elif self.conveyor_belt[0] == 'widget':
            self.add_item_to_holding_area(self.conveyor_belt.pop(0))
            self.conveyor_belt.insert(0, "empty")
        elif self.conveyor_belt[0] == "empty":
            pass
        print(self.holding_area)
        print(self.conveyor_belt)

