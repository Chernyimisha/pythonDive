# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple. Каждый объект хранит:
# имя файла без расширения или название каталога, расширение, если это файл, флаг каталога,
# название родительского каталога. Написать 3-5 тестов к задаче.
import argparse
import os
from pathlib import Path
from collections import namedtuple


def dir_parser(directory):
    """
    Функция, которая получает на вход путь до директории на ПК, рекурсивно собирает информацию о содержимом в
    виде объектов namedtuple. Каждый объект хранит: имя файла без расширения или название каталога, расширение,
    если это файл, флаг каталога (в данной версии использован шаблон флага), название родительского каталога.

    :param directory: <class str>
    :return: list[<class namedtuple>]
    """
    result = []
    Folder = namedtuple('Folder', ['name', 'flag', 'parent_dir'])
    File = namedtuple('File', ['name', 'extension', 'parent_dir'])
    for dir_path, dir_name, file_name in os.walk(directory):
        parent_dir = os.path.split(dir_path)[1]
        for d in dir_name:
            result.append(Folder(d, 'flag_folder', parent_dir))
        for f in file_name:
            name = os.path.splitext(f)[0]
            extension = os.path.splitext(f)[1]
            result.append(File(name, extension, parent_dir))
    return result


def cl_parser():
    default_dir = os.getcwd()
    parser = argparse.ArgumentParser(description='Parser directory')
    parser.add_argument('-l', '--link', default=default_dir)
    args = parser.parse_args()
    return dir_parser(args.link)


if __name__ == '__main__':

    for item in cl_parser():
        print(item)







