import random
from worker import Worker


class Factory:

    def __init__(self):
        self.conveyor_belt = []
        self.worker = Worker()
        self.holding_area = []
        self.recycling_bin = []

# method to add an item to the conveyor belt
    def add_to_conveyor_belt(self, item):
        self.conveyor_belt.append(item)

# adds random items either wotsit, widget or empty to the conveyor belt
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

# takes item from conveyor belt and adds it to the holding area if it is empty
    def add_item_to_holding_area(self, item):
        self.holding_area.append(item)
        self.conveyor_belt.insert(0, "empty")

# worker checks if they need the item being held. If they dont take it then it is put back onto the conveyor belt
    def worker_assessment_of_holding_area(self):
        if self.holding_area.__len__() == 1:
            held_item = self.holding_area[0]
            self.worker.check_item_in_holding_area(held_item)
            self.conveyor_belt.pop(0)
            self.conveyor_belt.insert(0, held_item)

# puts item into holding area and replaces the location in the list with an "empty" item
    def check_object_at_position_zero(self):
        if self.conveyor_belt[0] == "wotsit":
            self.add_item_to_holding_area(self.conveyor_belt.pop(0))
        elif self.conveyor_belt[0] == 'widget':
            self.add_item_to_holding_area(self.conveyor_belt.pop(0))
        elif self.conveyor_belt[0] == "empty":
            pass
        print(self.holding_area)
        print(self.conveyor_belt)

