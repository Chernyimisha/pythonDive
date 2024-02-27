import csv
import json
from random import randint
from typing import Callable


def save_to_json(func: Callable) -> Callable:
    # Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
    # Декоратор выполняет следующие действия:
    # Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
    # Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
    # Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c
    # и результаты вычислений.
    # Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет
    # сохранена информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.

    result_file = 'results.json'
    json_data = []

    def wrapper(*args):
        source_file = args[0]
        with (open(source_file, 'r', newline='') as f_csv,
              open(result_file, 'w') as f_json):
            csv_file = csv.reader(f_csv)
            for line in csv_file:
                params = [int(i) for i in line]
                print(params)
                json_data.append(dict(parameters=params, result=func(*params)))
            json.dump(json_data, f_json, indent=2)
        return func
    return wrapper


@save_to_json
def find_roots(a: int, b: int, c: int) -> None | float | int | tuple:
    # Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0.
    # Функция принимает три аргумента:
    # a, b, c (целые числа) - коэффициенты квадратного уравнения.

    # Функция возвращает:
    # None, если уравнение не имеет корней (дискриминант отрицателен).
    # Одно число, если уравнение имеет один корень (дискриминант равен нулю).
    # Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

    discriminant = b ** 2 - 4 * a * c
    print(discriminant)
    if discriminant > 0:
        return (-b + discriminant ** 0.5) / 2 * a, (-b - discriminant ** 0.5) / 2 * a
    elif discriminant == 0:
        return -b / 2 * a
    else:
        return None


def generate_csv_file(file_name, rows):
    # Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в
    # каждой строке, от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:
    # file_name (строка) - имя файла, в который будут записаны данные.
    # rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.
    list_set_params = [(randint(-1000, 1000), randint(-1000, 1000), randint(-1000, 1000)) for _ in range(rows)]
    with open(file_name, 'w', newline='') as f:
        csv_writer = csv.writer(f, dialect='excel', delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        for row in list_set_params:
            csv_writer.writerow(row)

generate_csv_file('input_data.csv', 101)
find_roots('input_data.csv')

with open("results.json", 'r') as f:
    data = json.load(f)

print(len(data))


