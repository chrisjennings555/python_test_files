class Worker:

    def __init__(self):
        self.basket = []

# adds an item to the worker basket
    def add_item_to_basket(self, item):
        self.basket.append(item)

# checks the item in the holding area and will add to the basket if they require the item
    def check_item_in_holding_area(self, held_list):
        if held_list == "empty" or held_list in self.basket:
            pass
        else:
            self.add_item_to_basket(held_list)

# checks whether the worker basket contains both items required to build a thingamajig and returns a boolean
    def check_items_ready_for_build(self):
        return bool(self.basket.__contains__("widget" and "wotsit"))

# # if the check_items_ready_for_build returns true this method clears the basket and creates a thingamajig object
#     def build_thingamajig(self):
#         if self.check_items_ready_for_build():
#             self.basket.clear()
#             self.basket.append("thingamajig")
#
# # pop thingamajig object from basket and return the object to send back to the holding area
#     def send_thingamajig_to_holding_area(self):
#         thingamajig = self.basket.pop()
#         return thingamajig

