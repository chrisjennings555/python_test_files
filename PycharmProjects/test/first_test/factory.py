import random
from collections import Counter
from worker import Worker


class Factory:

    def __init__(self):
        self.number_of_items = 100
        self.conveyor_belt = []
        self.worker1 = Worker()
        self.worker2 = Worker()
        self.worker3 = Worker()
        self.worker4 = Worker()
        self.worker5 = Worker()
        self.worker6 = Worker()
        self.recycling_bin = []

# method to add an item to the conveyor belt
    def add_to_conveyor_belt(self, item):
        self.conveyor_belt.append(item)

# adds random items either wotsit, widget or empty to the conveyor belt
    def add_random_items_to_conveyor_belt(self):
        for i in range(0, self.number_of_items):
            x = random.randint(0, 2)
            if x == 1:
                self.add_to_conveyor_belt("wotsit")
            elif x == 2:
                self.add_to_conveyor_belt("widget")
            elif x == 0:
                self.add_to_conveyor_belt("empty")

# takes the item at position zero and gives it to the worker
    def get_item_at_position_zero_to_workers(self):
        inspected_item = self.conveyor_belt.pop(0)
        # print(inspected_item, "inspected item")
        return inspected_item

# assesses conveyor belt and worker1 basket and places thingamajig if appropriate
    def worker1_places_thingamajig_onto_conveyor_belt(self):
        if self.conveyor_belt[0] == "empty":
            if self.worker1.basket.__contains__("thingamajig"):
                self.conveyor_belt.pop(0)
                self.conveyor_belt.insert(0, self.worker1.basket.pop())

# assesses conveyor belt and worker2 basket and places thingamajig if appropriate
    def worker2_places_thingamajig_onto_conveyor_belt(self):
        if self.conveyor_belt[0] == "empty":
            if self.worker2.basket.__contains__("thingamajig"):
                self.conveyor_belt.pop(0)
                self.conveyor_belt.insert(0, self.worker2.basket.pop())

# assesses conveyor belt and worker3 basket and places thingamajig if appropriate
    def worker3_places_thingamajig_onto_conveyor_belt(self):
        if self.conveyor_belt[0] == "empty":
            if self.worker3.basket.__contains__("thingamajig"):
                self.conveyor_belt.pop(0)
                self.conveyor_belt.insert(0, self.worker3.basket.pop())

# assesses conveyor belt and worker4 basket and places thingamajig if appropriate
    def worker4_places_thingamajig_onto_conveyor_belt(self):
        if self.conveyor_belt[0] == "empty":
            if self.worker4.basket.__contains__("thingamajig"):
                self.conveyor_belt.pop(0)
                self.conveyor_belt.insert(0, self.worker4.basket.pop())

# assesses conveyor belt and worker5 basket and places thingamajig if appropriate
    def worker5_places_thingamajig_onto_conveyor_belt(self):
        if self.conveyor_belt[0] == "empty":
            if self.worker5.basket.__contains__("thingamajig"):
                self.conveyor_belt.pop(0)
                self.conveyor_belt.insert(0, self.worker5.basket.pop())

# assesses conveyor belt and worker6 basket and places thingamajig if appropriate
    def worker6_places_thingamajig_onto_conveyor_belt(self):
        if self.conveyor_belt[0] == "empty":
            if self.worker6.basket.__contains__("thingamajig"):
                self.conveyor_belt.pop(0)
                self.conveyor_belt.insert(0, self.worker6.basket.pop())

# worker1 inspects the item it is handed and then places something back onto the conveyor belt
    def pass_inspected_item_to_worker_1(self):
        item = self.get_item_at_position_zero_to_workers()
        handled_item = self.worker1.does_worker_need_item(item)
        self.place_item_back_onto_conveyor_at_position_zero(handled_item)

# worker2 inspects the item it is handed and then places something back onto the conveyor belt
    def pass_inspected_item_to_worker_2(self):
        item = self.get_item_at_position_zero_to_workers()
        handled_item = self.worker2.does_worker_need_item(item)
        self.place_item_back_onto_conveyor_at_position_zero(handled_item)

# worker3 inspects the item it is handed and then places something back onto the conveyor belt
    def pass_inspected_item_to_worker_3(self):
        item = self.get_item_at_position_zero_to_workers()
        handled_item = self.worker3.does_worker_need_item(item)
        self.place_item_back_onto_conveyor_at_position_zero(handled_item)

# worker4 inspects the item it is handed and then places something back onto the conveyor belt
    def pass_inspected_item_to_worker_4(self):
        item = self.get_item_at_position_zero_to_workers()
        handled_item = self.worker4.does_worker_need_item(item)
        self.place_item_back_onto_conveyor_at_position_zero(handled_item)

# worker5 inspects the item it is handed and then places something back onto the conveyor belt
    def pass_inspected_item_to_worker_5(self):
        item = self.get_item_at_position_zero_to_workers()
        handled_item = self.worker5.does_worker_need_item(item)
        self.place_item_back_onto_conveyor_at_position_zero(handled_item)

# worker6 inspects the item it is handed and then places something back onto the conveyor belt
    def pass_inspected_item_to_worker_6(self):
        item = self.get_item_at_position_zero_to_workers()
        handled_item = self.worker6.does_worker_need_item(item)
        self.place_item_back_onto_conveyor_at_position_zero(handled_item)

# places the handles item back onto the conveyor belt
# this method is called in pass_inspected_item_to_worker_1
    def place_item_back_onto_conveyor_at_position_zero(self, item):
        self.conveyor_belt.insert(0, item)

# the item at position zero on the conveyor belt is then sent to recycling after being inspected
    def dispose_of_item_at_position_zero(self):
        disposed_item = self.conveyor_belt.pop(0)
        self.recycling_bin.append(disposed_item)

# uses built in python method to count the number of instances of something in a list
    def assess_recycling_bin(self):
        print("What's in the bin post run?", Counter(self.recycling_bin))

# main method to run the factory
    def run_factory(self):
        factory.add_random_items_to_conveyor_belt()
        print("length of conveyor belt pre run =", factory.conveyor_belt.__len__())
        for i in range(0, self.number_of_items):
            # worker1 does their magic with the item
            factory.worker1.check_items_ready_to_build_thingamajig()
            factory.worker1_places_thingamajig_onto_conveyor_belt()
            factory.pass_inspected_item_to_worker_1()
            # worker2 does their magic with the item
            factory.worker2.check_items_ready_to_build_thingamajig()
            factory.worker2_places_thingamajig_onto_conveyor_belt()
            factory.pass_inspected_item_to_worker_2()
            # worker3 does their magic with the item
            factory.worker3.check_items_ready_to_build_thingamajig()
            factory.worker3_places_thingamajig_onto_conveyor_belt()
            factory.pass_inspected_item_to_worker_3()
            # worker4 does their magic with the item
            factory.worker4.check_items_ready_to_build_thingamajig()
            factory.worker4_places_thingamajig_onto_conveyor_belt()
            factory.pass_inspected_item_to_worker_4()
            # worker5 does their magic with the item
            factory.worker5.check_items_ready_to_build_thingamajig()
            factory.worker5_places_thingamajig_onto_conveyor_belt()
            factory.pass_inspected_item_to_worker_5()
            # worker6 does their magic with the item
            factory.worker6.check_items_ready_to_build_thingamajig()
            factory.worker6_places_thingamajig_onto_conveyor_belt()
            factory.pass_inspected_item_to_worker_6()
            # factory then sends item into recycling
            factory.dispose_of_item_at_position_zero()
        print("length of conveyor belt post run =", factory.conveyor_belt.__len__())
        factory.assess_recycling_bin()



factory = Factory()

factory.run_factory()

# print(factory.conveyor_belt, "conveyor before")
# factory.worker_places_thingamajig_onto_conveyor_belt()
# factory.pass_inspected_item_to_worker_1()
# print('worker1 basket', factory.worker1.basket)
# factory.dispose_of_item_at_position_zero()
# print("recycling", factory.recycling_bin)
# print("conveyor post run", factory.conveyor_belt)
