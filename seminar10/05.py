# Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal и добавляют дополнительные атрибуты
# и методы:
#
# Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который возвращает длину крыла птицы.
#
# Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который возвращает категорию глубины рыбы
# (мелководная, средневодная, глубоководная) в зависимости от значения max_depth.
# Если максимальная глубина обитания рыбы (max_depth) меньше 10, то она относится к категории "Мелководная рыба".
# Если максимальная глубина обитания рыбы больше 100, то она относится к категории "Глубоководная рыба".
# В противном случае, рыба относится к категории "Средневодная рыба".
#
# Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию млекопитающего
# (Малявка, Обычный, Гигант) в зависимости от веса. Если вес объекта меньше 1, то он относится к категории "Малявка".
# Если вес объекта больше 200, то он относится к категории "Гигант".
# В противном случае, объект относится к категории "Обычный".


class Animal:
    def __init__(self, name: str):
        self.name = name


class Bird(Animal):
    def __init__(self, name: str, wingspan: float | int):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2


class Fish(Animal):
    def __init__(self, name: str, max_depth: float | int):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return 'Мелководная рыба'
        elif self.max_depth > 100:
            return 'Глубоководная рыба'
        return 'Средневодная рыба'


class Mammal(Animal):
    def __init__(self, name: str, weight: float | int):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return 'Малявка'
        elif self.weight > 200:
            return 'Гигант'
        return 'Обычный'


class AnimalFactory:

    @staticmethod
    def create_animal(animal_type: str, *args):
        if animal_type.lower() == 'bird':
            return Bird(*args)
        elif animal_type.lower() == 'fish':
            return Fish(*args)
        elif animal_type.lower() == 'mammal':
            return Mammal(*args)
        raise ValueError('Недопустимый тип животного')


if __name__ == '__main__':
    #     b = Bird('Bird1', 2.5)
    #     f = Fish('Fish1', 2.5)
    #     m = Mammal('Mammal1', 2.5)
    #
    # print(f'{b.wing_length()=}')
    # print(f'{f.depth()=}')
    # print(f'{m.category()=}')
    animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
    animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
    animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)
    animal4 = AnimalFactory.create_animal('Mamal', 'Слон', 5000)
    print(animal1.wing_length())
    print(animal2.depth())
    print(animal3.category())

