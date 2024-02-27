# Создайте функцию-замыкание, которая запрашивает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.

from random import randint


def game(number_secret: int, count: int):
    if not 1 <= number_secret <= 100:
        number_secret = randint(1, 100)
    if not 1 <= count <= 10:
        count = randint(1, 10)

    def run():
        for _ in range(count):
            answer = int(input('Угадайте число: '))
            if number_secret == answer:
                return True
        return False
    return run


if __name__ == '__main__':

    enter_ = game(5, 7)
    enter_()




