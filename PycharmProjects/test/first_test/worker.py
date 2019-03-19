class Worker:

    def __init__(self):
        self.basket = []

# adds an item to the worker basket
    def add_item_to_basket(self, item):
        self.basket.append(item)

# checks the item being passed from the conveyor belt and will add to the basket if they require the item
    def does_worker_need_item(self, item):
        if item == "empty":
            return item
        elif item == "thingamajig":
            return item
        elif self.basket.__contains__(item):
            return item
        elif self.basket.__contains__("thingamajig"):
            return item
        else:
            self.add_item_to_basket(item)
            handled_item = "empty"
            return handled_item

# if both wotsit and widget present in basket then clear basket and then create thingamajig
    def check_items_ready_to_build_thingamajig(self):
        if self.basket.__contains__("wotsit") and self.basket.__contains__("widget"):
            self.basket.clear()
            self.basket.append("thingamajig")



