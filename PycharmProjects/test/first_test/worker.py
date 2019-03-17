class Worker:

    def __init__(self):
        self.basket = []

    def add_item_to_basket(self, item):
        # adds an item to the worker basket
        self.basket.append(item)

    def check_item_in_holding_area(self, item):
        # checks the item in the holding area and will add to the basket if they require the item
        if item == "empty" or item in self.basket:
            pass
        else:
            self.add_item_to_basket(item)
        print(self.basket)

    def check_items_ready_for_build(self):
        result = bool(self.basket.__contains__("widget" and "wotsit"))
        return result

    def build_thingamajig(self):
        if self.check_items_ready_for_build():
            self.basket.clear()
            self.basket.append("thingamajig")

    def send_thingamajig_to_holding_area(self):
        thingamajig = self.basket.pop()
        return thingamajig
