class Side:
    def __init__(self, min_val: int = 1, max_val: int = 100):
        self._min_val = min_val
        self._max_val = max_val

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)

    def validate(self, value):
        if not self._min_val <= value <= self._max_val:
            raise ValueError('Некорректное значение!')


class Rectangle:
    width = Side()
    height = Side(2, 9)

    def __init__(self, width: int, height: int = None):
        self.width = width
        self.height = height if height != width else width

    # @property
    # def height(self):
    #     return self.height
    #
    # @height.setter
    # def height(self, value):
    #     self.height = value
    #
    # @property
    # def width(self):
    #     return self.width
    #
    # @_width.setter
    # def width(self, value):
    #     self.width = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return int(2 * (self.width + self.height))

    def __add__(self, other):
        new_perimetr = self.perimeter() + other.perimeter()
        new_height = self.height + other.height
        new_width = int(new_perimetr / 2 - new_height)
        return Rectangle(new_width, new_height)

    def __sub__(self, other):
        new_perimetr = abs(self.perimeter() - other.perimeter())
        new_width = abs(self.width - other._width)
        new_height = int(new_perimetr / 2 - new_width)
        if new_height < 0:
            raise ValueError('Вычитание данных прямоугольников невозможно!')
        return Rectangle(new_width, new_height)

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

if __name__ == '__main__':
    P1 = Rectangle(4, 8)
    P2 = Rectangle(6, 15)
    # print(P1 + P2)
    # print(P1 - P2)

