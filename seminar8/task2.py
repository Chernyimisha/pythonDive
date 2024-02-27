# Задача 2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7). После каждого ввода добавляйте
# новую информацию в JSON файл. Пользователи
# группируются по уровню доступа. Идентификатор
# пользователя выступает ключём для имени. Убедитесь,
# что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные
# в файл данные должны сохраняться.

# Задача 3
# Напишите функцию, которая сохраняет созданный
# в прошлом задании файл в формате CSV.

import json
import os


# def add_usrs_json(filename: str = 'users.json'):
#     """Добавление пользователей в json файл."""
#     while True:
#         try:
#             with open(filename, 'r') as src:
#                 data = json.load(src)
#         except FileNotFoundError:
#             data = {str(i): [] for i in range(1, 8)}
#
#         name = input('Ввведите имя: ')
#         user_id = input('Введите ваш id: ')
#         level = input('Введите ваш уровень доступа: ')
#         data[level].append({'name': name, 'id': user_id})
#
#         with open(filename, 'w') as res:
#             json.dump(data, res, indent=4)
#
#
# def json_to_csv(src_file: str = 'users.json',
#                 out_file: str = 'users.csv'):
#     """Перевод из формата json в csv."""
#     with open(src_file, 'r') as src:
#         data = json.load(src)
#
#     with open(out_file, 'w') as res:
#         res.write('id,level,name')
#         for level, users_lst in data.items():
#             for user in users_lst:
#                 res.write(f'\n{user["id"]},{level},{user["name"]}')

# {level: {id: name}}


def load_or_create(file_name: str):
    if file_name in os.listdir():
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data

    with open(file_name, 'w') as f:
        json.dump({}, f)
    return {}


def enter_users(level: str, id: str, name: str, file_name: str) -> None:
    data = load_or_create(file_name)
    for value in data.values():
        if id in value:
            raise ValueError("id уже существует")

    data.setdefault(level, {})
    data[level].setdefault(id, name)

    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


# Задача 4
# Прочитайте созданный в прошлом задании csv файл
# без использования csv.DictReader. Дополните id до
# 10 цифр незначащими нулями. В именах первую букву
# сделайте прописной. Добавьте поле хеш на основе имени
# и идентификатора. Получившиеся записи сохраните в json
# файл, где каждая строка csv файла представлена как
# отдельный json словарь. Имя исходного и конечного
# файлов передавайте как аргументы функции.

####################################### ВАРИАНТ ПРЕПОДАВАТЕЛЯ
def csv_to_json(src_file: str = 'users.csv',
                out_file: str = 'users_1.json', ):
    """Перевод из csv к json формату."""
    with open(src_file, 'r') as src:
        data = list(map(lambda x: x.split(','), src.read().split('\n')))

    for i in range(1, len(data)):
        data[i][0] = data[i][0].zfill(10)
        data[i][2] = data[i][2].capitalize()

        user_id = data[i][0]
        name = data[i][2]
        data[i].append(hash(user_id + name))

    data = data[1::]
    print(data)

    data = [{'id': u_id, 'level': level, 'name': uname, 'hash': uhash}
            for u_id, level, uname, uhash in data]

    with open(out_file, 'w') as res:
        json.dump(data, res, indent=4)

####################################### ВАРИАНТ ПРЕПОДАВАТЕЛЯ

import csv


def json_to_csv(json_in: str, csv_out: str) -> None:
    with (
        open(json_in, 'r', newline='', encoding='utf-8') as f_in,
        open(csv_out, 'w', newline='', encoding='utf-8') as f_out,
    ):
        data = json.load(f_in)
    all_data = []
    csv_write = csv.DictWriter(f_out, fieldnames=['level', 'id', 'name'])
    for level, inner_dict in data.items():
        for id_, name in inner_dict.items():
            all_data.append({"id": id_, "level": level, "name": name})
            csv_write.writeheader()
            csv_write.writerows(all_data)


if __name__ == '__main__':
    # while True:
    #     level = input('Введите уровень доступа: ')
    #     id = input('Введите идентификатор: ')
    #     name = input('Введите имя: 1')
    #     enter_users(level, id, name, 'database.json')

    json_to_csv('database.json', 'task02.csv')

