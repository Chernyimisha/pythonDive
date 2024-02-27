# Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту директорию и
# все вложенные директории. Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle.
# Каждый результат должен содержать следующую информацию:
#
# Путь к файлу или директории: Абсолютный путь к файлу или директории.
# Тип объекта: Это файл или директория.
# Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах.
#
# Важные детали:
#
# Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
#
# Для файлов сохраните их размер в байтах.
#
# Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной директории,
# и вложенных директорий.
#
# Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
#
# Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.
#
# Для обхода файловой системы вы можете использовать модуль os.
#
# Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории и возвращать
# результаты в виде списка словарей. После этого результаты должны быть сохранены в трех различных файлах
# (JSON, CSV и Pickle) с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.
#


import json
import csv
import pickle
import os


def get_dir_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            total_size += size
        for name in dirs:
            path = os.path.join(root, name)
            total_size += get_dir_size(path)
    return total_size


def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})
        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})
    return results


def save_results_to_json(results, output_file):
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)


def save_results_to_csv(results, output_file):
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Path', 'Type', 'Size'])
        writer.writeheader()
        writer.writerows(results)


def save_results_to_pickle(results, output_file):
    with open(output_file, 'wb') as f:
        pickle.dump(results, f)

directory = 'M:\РАБОТА МИША\Курс Python\Projects Python\PYTHON Dive'
results = traverse_directory(directory)

save_results_to_json(results, 'results.json')
save_results_to_csv(results, 'results.csv')
save_results_to_pickle(results, 'results.pickle')

