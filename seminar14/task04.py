class Side:
    def __init__(self, min_len, max_len) -> None:
        self.min_len = min_len
        self.max_len = max_len

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if value < self.min_len or value > self.max_len:
            raise ValueError


class Rectangle:
    """
    >>> Rectangle(4,8).area()
    32
    >>> Rectangle(4,8) + Rectangle(2, 4)
    Rectangle(self._height=6, self._width=12.0)
    >>> Rectangle(4,8) - Rectangle(2, 4)
    Rectangle(self._height=2, self._width=4.0)
    """
    _height = Side(1, 10000)
    _width = Side(1, 10000)

    def __init__(self, height, width=None) -> None:
        self._height = height
        if width:
            self._width = width
        else:
            self._width = height

# @property
# def height(self):
# return self._height

# @property
# def width(self):
# return self._width

# @height.setter
# def height(self, value):
# if value <= 0:
# raise ValueError
# self._height = value

# @width.setter
# def width(self, value):
# if value <= 0:
# raise ValueError
# self._width = value

    def __repr__(self):
        return f"Rectangle({self._height=}, {self._width=})"

    def per(self):
        return 2 * (self._height + self._width)

    def area(self):
        return self._height * self._width

    def __add__(self, obj: "Rectangle"):
        new_per = self.per() + obj.per()
        new_height = self._height + obj._height
        new_width = (new_per / 2) - new_height
        if new_width <= 0 or new_height <= 0:
            raise ValueError
        return Rectangle(new_height, new_width)

    def __sub__(self, obj: "Rectangle"):
        new_per = self.per() - obj.per()
        new_height = self._height - obj._height
        new_width = (new_per / 2) - new_height
        if new_width <= 0 or new_height <= 0:
            raise ValueError
        return Rectangle(new_height, new_width)

    def __eq__(self, obj: "Rectangle") -> bool:
        return self.area() == obj.area()

    def __gt__(self, obj: "Rectangle") -> bool:
        return self.area() > obj.area()

    def __lt__(self, obj: "Rectangle") -> bool:
        return self.area() < obj.area()


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)