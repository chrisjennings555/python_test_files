# # puts first item from conveyor belt into holding area
# # FIRST METHOD CALLED
#     def move_item_at_position_zero_to_holding_area(self):
#         self.holding_area.append(self.conveyor_belt.pop(0))
#
# # worker checks if they need the item being held. holding area will be emptied
# # SECOND METHOD CALLED
#     def worker_assessment_of_holding_area(self):
#         self.worker.check_item_in_holding_area(self.holding_area.pop(0))
#
# # checks whether the holding area is empty - returns boolean
# # this method is called in replace_item_taken_from_holding_area_with_empty
#     def did_worker_take_item_from_holding_area(self):
#         return bool(self.holding_area.__len__() == 0)
#
# # will replace item taken from holding area with an empty
# # THIRD METHOD CALLED
#     def replace_item_taken_from_holding_area_with_empty(self):
#         if self.did_worker_take_item_from_holding_area():
#             self.holding_area.append("empty")
#
# # check to see if worker basket contains both items, clears the basket and populates with thingamajig
# # FOURTH METHOD CALLED
#     def worker_builds_thingamajig(self):
#         if self.worker.check_items_ready_for_build():
#             self.worker.basket.clear()
#             self.worker.basket.append("thingamajig")
#         else:
#             return "not ready"
#
# # sends created thingamajig to holding area
# # FIFTH METHOD CALLED - WILL ONLY EXECUTE IF WORKER BASKET CONTAINS THINGAMAJIG
#     def send_thingamajig_to_holding_area(self):
#         self.holding_area.append(self.worker.basket.pop(0))
#
# # put the item in the holding area back onto the conveyor belt
# # SIXTH METHOD CALLED
#     def put_item_in_holding_area_back_onto_conveyor_belt(self):
#         self.conveyor_belt.insert(0, self.holding_area.pop(0))
#
# # sends thingamajig to conveyor belt if the space at position zero is empty
# # SEVENTH METHOD CALLED - WILL ONLY EXECUTE IF HOLDING AREA CONTAINS THINGAMAJIG
# #     def send_completed_thingamajig_back_to_conveyor_belt(self):
# #         if self.holding_area.__contains__("thingamajig"):
# #             if self.conveyor_belt[0] == "empty":
# #                 self.conveyor_belt.pop(0)
# #                 self.conveyor_belt.insert(0, self.holding_area.pop(0))
#
# # after checks are complete sends item at position 0 to finished products or recycling
# # EIGHTH METHOD CALLED
#     def send_to_recycling(self):
#         if self.conveyor_belt[0] is not "thingamajig":
#             self.recycling_bin.append(self.conveyor_belt.pop(0))
#
# # perform all functions in running factory with one method
#     def run_factory(self):
#         for i in range(0, 10):
#             self.move_item_at_position_zero_to_holding_area()
#             self.worker_assessment_of_holding_area()
#             self.replace_item_taken_from_holding_area_with_empty()
#             if self.worker_builds_thingamajig():
#                 self.send_thingamajig_to_holding_area()
#                 self.put_item_in_holding_area_back_onto_conveyor_belt()
#                 # self.send_completed_thingamajig_back_to_conveyor_belt()
#             else:
#                 self.put_item_in_holding_area_back_onto_conveyor_belt()
#             self.send_to_recycling()

# def test_item_placed_in_holding_area(self):
#     factory = Factory()
#     factory.add_random_items_to_conveyor_belt()
#     factory.move_item_at_position_zero_to_holding_area()
#     self.assertEqual(factory.holding_area.__len__(), 1)
#
#
# def test_items_moved_from_belt_to_holding_area_and_reverse(self):
#     factory = Factory()
#     factory.add_random_items_to_conveyor_belt()
#     factory.move_item_at_position_zero_to_holding_area()
#     factory.worker_assessment_of_holding_area()
#     self.assertEqual(factory.conveyor_belt.__len__(), 10)
#
#
# def test_item_sent_to_recycling(self):
#     factory = Factory()
#     factory.add_random_items_to_conveyor_belt()
#     factory.move_item_at_position_zero_to_holding_area()
#     factory.worker_assessment_of_holding_area()
#     factory.send_to_recycling()
#     print("after running once", factory.conveyor_belt)
#     print("worker basket PR", factory.worker.basket)
#     print("recycling PR", factory.recycling_bin)
#     self.assertEqual(factory.recycling_bin.__len__(), 1)
#     self.assertEqual(factory.conveyor_belt.__len__(), 9)
#
#
# def test_factory_can_run(self):
#     factory = Factory()
#     factory.add_random_items_to_conveyor_belt()
#     print("initial conveyor order", factory.conveyor_belt)
#     factory.run_factory()
#     print("recycling after run", factory.recycling_bin)
#     self.assertEqual(factory.conveyor_belt.__len__(), 0)