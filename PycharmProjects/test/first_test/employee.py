import random


class Employee:

    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        self.basket = []
        self.worker = []
        self.holding_area = []

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def add_to_basket(self, item):
        self.basket.append(item)

    def add_random_stuff_to_basket(self):
        for i in range(0, 10):
            x = random.randint(0, 2)
            if x == 1:
                self.basket.append("wotsit")
            elif x == 2:
                self.basket.append("thingy")
            elif x == 0:
                self.basket.append("empty")

        print(self.basket)

    def add_item_to_holding_area(self, item):
        self.holding_area.append(item)

    def check_object_at_position_zero(self):
        if self.basket[0] == "wotsit":
            self.add_item_to_holding_area(self.basket.pop(0))
        elif self.basket[0] == 'thingy':
            self.add_item_to_holding_area(self.basket.pop(0))
        elif self.basket[0] == "empty":
            pass

    def check_wotsit_not_in_basket(self, wotsit):
        if "wotsit" not in self.worker:
            self.worker.append(wotsit)

    def check_thingy_not_in_basket(self, thingy):
        if "thingy" not in self.worker:
            self.worker.append(thingy)

    def add_item_to_worker_basket(self):
        if self.holding_area.__len__() == 1:
            new_item = self.holding_area.pop()
            self.worker.append(new_item)
        else:
            pass

    def run_conveyor_belt(self):
        self.add_random_stuff_to_basket()

        for i in range(1, self.basket.__len__()):
            self.check_object_at_position_zero()
            self.add_item_to_worker_basket()
            print(self.worker)

