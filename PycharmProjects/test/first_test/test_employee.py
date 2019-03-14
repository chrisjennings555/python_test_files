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
