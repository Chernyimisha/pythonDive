# Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных разных типов на основе переданного
# типа и параметров. Класс-фабрика должен иметь метод create_animal, который принимает следующие аргументы:
#
# animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal').
# *args - переменное количество аргументов, представляющих параметры для конкретного типа животного. Количество и типы
# аргументов могут различаться в зависимости от типа животного.
#
# Метод create_animal должен создавать и возвращать экземпляр животного заданного типа с переданными параметрами.
#
# Если animal_type не соответствует 'Bird', 'Fish' или 'Mammal', функция вызовет ValueError с сообщением
# 'Недопустимый тип животного'.


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

    animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
    animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
    animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)
    animal4 = AnimalFactory.create_animal('Mamal', 'Слон', 5000)
    print(animal1.wing_length())
    print(animal2.depth())
    print(animal3.category())
