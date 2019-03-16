import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_employee_has_first_name(self):
        emp1 = Employee('Chris', 'Jennings', 50000)
        self.assertEqual(emp1.first, 'Chris')

    def test_employee_has_last_name(self):
        emp1 = Employee('Chris', 'Jennings', 50000)
        self.assertEqual(emp1.last, 'Jennings')

    def test_employee_has_pay(self):
        emp1 = Employee('Chris', 'Jennings', 50000)
        self.assertEqual(emp1.pay, 50000)

    def test_employee_can_add_item_to_basket(self):
        emp1 = Employee('Chris', 'Jennings', 50000)
        emp1.add_to_basket(55)
        emp1.add_to_basket(55)
        emp1.add_to_basket(55)
        self.assertEqual(emp1.basket.__len__(), 3)

    def test_add_random_numbers_to_basket(self):
        emp1 = Employee('Chris', 'Jennings', 50000)
        emp1.add_random_stuff_to_basket()
        self.assertEqual(emp1.basket.__len__(), 10)

    def test_item_placed_in_holding_area(self):
        emp1 = Employee('Chris', 'Jennings', 50000)
        emp1.add_random_stuff_to_basket()
        emp1.check_object_at_position_zero()
        self.assertEqual(emp1.holding_area.__len__(), 1)

    def test_conveyor_belt_can_run(self):
        emp1 = Employee('Chris', 'Jennings', 50000)
        emp1.run_conveyor_belt()
        self.assertEqual(emp1.worker.__len__(), 3)
