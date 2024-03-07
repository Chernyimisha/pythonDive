import pytest
from seminar14.taskDZ_03 import Person, Employee


# class TestEmployee(pytest.TestCase):
@pytest.fixture
def emp1():
    return Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000.0)


def test_employee_full_name(emp1):
    assert emp1.full_name() == "Ivanov Ivan Ivanovich", 'Error'


def test_employee_birthday(emp1):
    emp1.birthday()
    assert emp1.get_age() == 31, 'Error'


def test_employee_raise_salary(emp1):
    emp1.raise_salary(10)
    assert emp1.salary == 55000.0, 'Error'


def test_employee_str(emp1):
    assert emp1.__str__() == "Ivanov Ivan Ivanovich (Manager)", 'Error'


def test_employee_last_name_title(emp1):
    assert emp1.last_name == "Ivanov", 'Error'


if __name__ == '__main__':
    # pytest.main(['-vv'])
    # Запускаем pytest.main() с нужными параметрами
    pytest.main(["--no-header", '-q', "--durations=0", new_filename])