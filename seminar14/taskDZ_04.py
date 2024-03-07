import unittest
from seminar14.taskDZ_03 import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000.0)
        self.emp.birthday()
        self.emp.raise_salary(10)

    def test_employee_full_name(self):
        self.assertEqual(self.emp.full_name(), "Ivanov Ivan Ivanovich", msg='FAILED (failures=1)')

    def test_employee_birthday(self):
        self.assertEqual(self.emp.get_age(), 31, msg='FAILED (failures=1)')

    def test_employee_raise_salary(self):
        self.assertEqual(self.emp.salary, 55000.0, msg='FAILED (failures=1)')

    def test_employee_str(self):
        self.assertEqual(self.emp.__str__(), "Ivanov Ivan Ivanovich (Manager)", msg='FAILED (failures=1)')

    def test_employee_last_name_title(self):
        self.assertEqual(self.emp.last_name == 'Ivan', False, msg='FAILED (failures=1)')


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # unittest.main()