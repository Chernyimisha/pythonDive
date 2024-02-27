# Задача №2
# Дорабатываем задачу 1. Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку числа
# в диапазоны [1, 100] и [1, 10]. Если не входят,
# вызывать функцию со случайными числами из диапазонов.

from random import randint


def game(func):

    def wrapper(number_secret, count):
        if not 1 <= number_secret <= 100:
            number_secret = randint(1, 100)
        if not 1 <= count <= 10:
            count = randint(1, 10)
        return func(number_secret, count)
    print('Enter game()')
    return wrapper


@game
def run(number_secret: int, count: int):
    for _ in range(count):
        answer = int(input('Угадайте число: '))
        if number_secret == answer:
            return True
    return False


if __name__ == '__main__':
    run(7, 15)