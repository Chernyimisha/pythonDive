# Задача 1
# Вспоминаем задачу 3 из прошлого семинара.
# Мы сформировали текстовый файл с псевдо именами
# и произведением чисел.
# Напишите функцию, которая создаёт из созданного
# ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.

import json


# def txt_json(src_file: str = 'text.txt',
#              out_file: str = 'text.json'):
#     """Импорт данных из .txt в .json"""
#     with open(src_file, 'r') as file:
#         names = dict(map(lambda x: tuple(x.split()),
#                          file.read().split('\n')))
#
#     with open(out_file, 'w') as file:
#         json.dump(names, file, indent=4)

def txt_to_json(source, output):
    data1 = {}
    with open(source, 'r') as f:
        data = f.read()

    for line in data.split('\n'):
        name, number = line.split(' ')
        data1[name.capitalize()] = float(number)

    with open(output, 'w') as f:
        json.dump(data1, f, indent=4)

txt_to_json('file.txt', 'output.json')