import pytest
from seminar13.taskDZ_01 import Rectangle, NegativeValueError


@pytest.fixture
def r1():
    return Rectangle(5)


@pytest.fixture
def r2():
    return Rectangle(3, 4)


@pytest.fixture
def r3():
    return Rectangle(5, 3)


@pytest.fixture
def r4():
    return Rectangle(1, 4)


def test_width(r1):
    assert r1.width == 5, 'Error'


def test_height(r2):
    assert r2.height == 4, 'Error'


def test_perimeter(r1):
    assert r1.perimeter() == 20, 'Error'


def test_area(r2):
    assert r2.area() == 12, 'Error'


def test_addition(r3, r4):
    r5 = r3 + r4
    assert r5.__str__() == 'Прямоугольник со сторонами 6 и 7.0', 'Error'


def test_negative_width():
    with pytest.raises(NegativeValueError):
        Rectangle(-3, 5)


def test_negative_height():
    with pytest.raises(NegativeValueError):
        Rectangle(3, -5)


def test_set_width(r1):
    r1.width = 10
    assert r1.width == 10, 'Error'


def test_set_negative_width(r1):
    with pytest.raises(NegativeValueError):
        r1.width = -10


def test_set_height(r2):
    r2.height = 6
    assert r2.height == 6, 'Error'


def test_set_negative_height(r2):
    with pytest.raises(NegativeValueError):
        r2.height = -6


def test_subtraction():
    r1 = Rectangle(10, 3)
    r2 = Rectangle(1, 4)
    with pytest.raises(NegativeValueError):
        r1 - r2


def test_subtraction_negative_result():
    r1 = Rectangle(10, 3)
    r2 = Rectangle(1, 4)
    with not pytest.raises(NegativeValueError):
        r1 - r2


def test_subtraction_same_perimeter():
    r1 = Rectangle(5, 4)
    r2 = Rectangle(1, 3)
    r3 = r1 - r2
    assert r3.__eq__(Rectangle(4, 1)) is True, 'Error'


if __name__ == '__main__':
    # Запускаем pytest.main() с нужными параметрами
    pytest.main(["--no-header", '-q', "--durations=0", new_filename])


