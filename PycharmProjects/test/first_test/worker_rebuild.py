class Worker:

    def __init__(self, assigned_slot):
        self.basket = []
        self.assigned_slot = assigned_slot

# adds an item to the worker basket
    def add_item_to_basket(self, item):
        self.basket.append(item)

# checks the item being passed from the conveyor belt and will add to the basket if they require the item
    def does_worker_need_item(self, item):
        if item == "thingamajig":
            return False
        elif item == "empty":
            return False
        elif self.basket.__contains__(item):
            return False
        elif self.basket.__contains__("thingamajig"):
            return False
        else:
            return True

# if both wotsit and widget present in basket then clear basket and then create thingamajig
    def if_ready_build_thingamajig(self):
        if self.basket.__contains__("wotsit") and self.basket.__contains__("widget"):
            self.basket.clear()
            self.basket.append("thingamajig")
