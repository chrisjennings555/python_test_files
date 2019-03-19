import random
from collections import Counter
from worker_rebuild import Worker


class Factory:

    def __init__(self):
        self.number_of_items = 100
        self.conveyor_belt = []
        self.slot1 = "empty"
        self.slot2 = "empty"
        self.slot3 = "empty"
        self.worker1 = Worker()
        self.worker2 = Worker()
        self.worker3 = Worker()
        self.worker4 = Worker()
        self.worker5 = Worker()
        self.worker6 = Worker()
        self.recycling_bin = []
        self.completed_thingamajigs = []

# method to add an item to the conveyor belt
    def add_to_conveyor_belt(self, item):
        self.conveyor_belt.append(item)

# method to add slots to conveyor belt
    def build_conveyor_belt(self):
        self.add_to_conveyor_belt(self.slot1)
        self.add_to_conveyor_belt(self.slot2)
        self.add_to_conveyor_belt(self.slot3)

# reassigns status of slot 1
    def set_slot_1(self, item):
        self.slot1 = item

# reassigns status of slot 2
    def set_slot_2(self, item):
        self.slot2 = item

# reassigns status of slot 3
    def set_slot_3(self, item):
        self.slot3 = item

# generates random item and adds to slot 1
    def add_random_item_to_slot_1(self):
        x = random.randint(0, 2)
        if x == 1:
            item = "wotsit"
            self.set_slot_1(item)
        elif x == 2:
            item = "widget"
            self.set_slot_1(item)
        elif x == 0:
            item = "empty"
            self.set_slot_1(item)

# worker1 assesses whether they require the item at slot1 and will add to basket if appropriate
    def worker1_assesses_item_in_slot_1(self):
        required_item = self.slot1
        if self.worker1.does_worker_need_item(required_item):
            self.worker1.add_item_to_basket(required_item)
            empty_item = "empty"
            self.set_slot_1(empty_item)

# performs check on status of workers basket and will build a thingamajig if appropriate
    def worker1_checks_and_builds_thingamajig(self):
        self.worker1.if_ready_build_thingamajig()

# will place a thingamajig onto the conveyor belt if they have one in their basket
    def worker1_places_thingamajig_onto_conveyor_belt(self):
        if self.slot1 == "empty":
            if self.worker1.basket.__contains__("thingamajig"):
                self.set_slot_1(self.worker1.basket.pop())

# worker2 assesses whether they require the item at slot1 and will add to basket if appropriate
    def worker2_assesses_item_in_slot_1(self):
        required_item = self.slot1
        if self.worker2.does_worker_need_item(required_item):
            self.worker2.add_item_to_basket(required_item)
            empty_item = "empty"
            self.set_slot_1(empty_item)

# performs check on status of workers basket and will build a thingamajig if appropriate
    def worker2_checks_and_builds_thingamajig(self):
        self.worker2.if_ready_build_thingamajig()

# will place a thingamajig onto the conveyor belt if they have one in their basket
    def worker2_places_thingamajig_onto_conveyor_belt(self):
        if self.slot1 == "empty":
            if self.worker2.basket.__contains__("thingamajig"):
                self.set_slot_1(self.worker2.basket.pop())

# worker3 assesses whether they require the item at slot2 and will add to basket if appropriate
    def worker3_assesses_item_in_slot_2(self):
        required_item = self.slot2
        if self.worker3.does_worker_need_item(required_item):
            self.worker3.add_item_to_basket(required_item)
            empty_item = "empty"
            self.set_slot_2(empty_item)

# performs check on status of workers basket and will build a thingamajig if appropriate
    def worker3_checks_and_builds_thingamajig(self):
        self.worker3.if_ready_build_thingamajig()

# will place a thingamajig onto the conveyor belt if they have one in their basket
    def worker3_places_thingamajig_onto_conveyor_belt(self):
        if self.slot2 == "empty":
            if self.worker3.basket.__contains__("thingamajig"):
                self.set_slot_2(self.worker3.basket.pop())

# worker4 assesses whether they require the item at slot2 and will add to basket if appropriate
    def worker4_assesses_item_in_slot_2(self):
        required_item = self.slot2
        if self.worker4.does_worker_need_item(required_item):
            self.worker4.add_item_to_basket(required_item)
            empty_item = "empty"
            self.set_slot_2(empty_item)

# performs check on status of workers basket and will build a thingamajig if appropriate
    def worker4_checks_and_builds_thingamajig(self):
        self.worker4.if_ready_build_thingamajig()

# will place a thingamajig onto the conveyor belt if they have one in their basket
    def worker4_places_thingamajig_onto_conveyor_belt(self):
        if self.slot2 == "empty":
            if self.worker4.basket.__contains__("thingamajig"):
                self.set_slot_2(self.worker4.basket.pop())

# worker5 assesses whether they require the item at slot3 and will add to basket if appropriate
    def worker5_assesses_item_in_slot_3(self):
        required_item = self.slot3
        if self.worker5.does_worker_need_item(required_item):
            self.worker5.add_item_to_basket(required_item)
            empty_item = "empty"
            self.set_slot_3(empty_item)

# performs check on status of workers basket and will build a thingamajig if appropriate
    def worker5_checks_and_builds_thingamajig(self):
        self.worker5.if_ready_build_thingamajig()

# will place a thingamajig onto the conveyor belt if they have one in their basket
    def worker5_places_thingamajig_onto_conveyor_belt(self):
        if self.slot3 == "empty":
            if self.worker5.basket.__contains__("thingamajig"):
                self.set_slot_3(self.worker5.basket.pop())

# worker6 assesses whether they require the item at slot3 and will add to basket if appropriate
    def worker6_assesses_item_in_slot_3(self):
        required_item = self.slot3
        if self.worker6.does_worker_need_item(required_item):
            self.worker6.add_item_to_basket(required_item)
            empty_item = "empty"
            self.set_slot_3(empty_item)

# performs check on status of workers basket and will build a thingamajig if appropriate
    def worker6_checks_and_builds_thingamajig(self):
        self.worker6.if_ready_build_thingamajig()

# will place a thingamajig onto the conveyor belt if they have one in their basket
    def worker6_places_thingamajig_onto_conveyor_belt(self):
        if self.slot3 == "empty":
            if self.worker6.basket.__contains__("thingamajig"):
                self.set_slot_3(self.worker6.basket.pop())

# adds new slot to position 0 of conveyor belt and moves original along one place
    def move_slot1_to_slot2(self):
        self.set_slot_2(self.slot1)

# moves slot at position zero to slot at position 1 (slot 2 becomes slot 3)
    def move_slot2_to_slot3(self):
        self.set_slot_3(self.slot2)

# moves contents of slot 3 into relevant area - either recycling or completed
    def dispose_of_item_in_slot_3(self):
        disposed_item = self.slot3
        if disposed_item == "thingamajig":
            self.completed_thingamajigs.append(disposed_item)
        else:
            self.recycling_bin.append(disposed_item)

# uses built in python method to count the number of instances of items in the recycling bin
    def assess_recycling_bin(self):
        print("Contents of recycling bin post run =", Counter(self.recycling_bin))

# uses built in python method to count the number of completed thingamajigs
    def assess_completed_thingamajigs(self):
        print("Number of completed thingamajigs =", self.completed_thingamajigs.__len__())

    def run_factory(self):
        factory.build_conveyor_belt()

        for i in range(0, factory.number_of_items):
            # each worker first gets chance to assess that is in the slot in front of them
            # if they cant pick up but have a thingamajig then it can be placed
            factory.worker1_assesses_item_in_slot_1()
            factory.worker1_places_thingamajig_onto_conveyor_belt()
            factory.worker2_assesses_item_in_slot_1()
            factory.worker2_places_thingamajig_onto_conveyor_belt()
            factory.worker3_assesses_item_in_slot_2()
            factory.worker3_places_thingamajig_onto_conveyor_belt()
            factory.worker4_assesses_item_in_slot_2()
            factory.worker4_places_thingamajig_onto_conveyor_belt()
            factory.worker5_assesses_item_in_slot_3()
            factory.worker5_places_thingamajig_onto_conveyor_belt()
            factory.worker6_assesses_item_in_slot_3()
            factory.worker6_places_thingamajig_onto_conveyor_belt()

            # each worker gets opportunity to build their thingamajig if they have each item
            factory.worker1_checks_and_builds_thingamajig()
            factory.worker2_checks_and_builds_thingamajig()
            factory.worker3_checks_and_builds_thingamajig()
            factory.worker4_checks_and_builds_thingamajig()
            factory.worker5_checks_and_builds_thingamajig()
            factory.worker6_checks_and_builds_thingamajig()

            # the item at slot 3 is sent to appropriate place and everything is moved along 1 slot
            factory.dispose_of_item_in_slot_3()
            factory.move_slot2_to_slot3()
            factory.move_slot1_to_slot2()
            factory.add_random_item_to_slot_1()

        # prints information about what is in the various end locations
        factory.assess_recycling_bin()
        factory.assess_completed_thingamajigs()


factory = Factory()
factory.run_factory()

# print("recycling bin =", factory.recycling_bin)
# print("worker1 basket =", factory.worker1.basket)
# print("worker2 basket =", factory.worker2.basket)
# print("post slot1 =", factory.slot1)
# print("post slot2 =", factory.slot2)
# print("post slot3 =", factory.slot3)
