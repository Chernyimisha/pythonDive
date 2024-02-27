# Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника. Складываем и вычитаем периметры,
# а не длинну и ширину. При вычитании не допускайте отрицательных значений.

class Rectangle:

    def __init__(self, width: int, height: int = None):
        self.width = width
        self.height = height if height != width else width

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
    rect1 = Rectangle(4, 5)
    rect2 = Rectangle(3, 3)

    print(rect1)
    print(rect2)

    print(rect1.perimeter())
    print(rect1.area())
    print(rect2.perimeter())
    print(rect2.area())

    rect_sum = rect1 + rect2
    rect_diff = rect1 - rect2

    print(rect_sum)
    print(rect_diff)

    print(rect1 < rect2)
    print(rect1 == rect2)
    print(rect1 <= rect2)

    print(repr(rect1))
    print(repr(rect2))
