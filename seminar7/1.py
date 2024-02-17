# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

import random


def create_file_number(quantity: int, filename: str):
    with open(filename, 'w') as f:
        for i in range(quantity):
            print(f'{random.randint(-1000, 1000)}|{random.uniform(-1000, 1000)}', file=f)


create_file_number(5, 'numbers.txt')


