# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
# исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории

# rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

import os
from pathlib import Path


def create_part_number(size: int, number: int):
    size_number = 0
    count_number = number
    result = ''
    while count_number >= 1:
        count_number /= 10
        size_number += 1
    while (size - size_number) > 0:
        result += '0'
        size -= 1
    return result + str(number)


def rename_files(link_dir='test_folder',
                 desired_name=None,
                 num_digits=3,
                 source_ext='txt',
                 target_ext='doc',
                 range_name=None,
                 ) -> None:
    count = 1
    dir_list = os.listdir(link_dir)
    for obj in dir_list:
        print(obj)
        if os.path.isfile(obj):
            old_name = obj.rpartition('.')[0]
            print(old_name)
            old_ext = obj.rpartition('.')[2]
            if old_ext == source_ext:
                if range_name is not None and range_name[0] <= len(old_name) and range_name[1] <= len(old_name):
                    new_name = old_name[range_name[0]-1:range_name[1]] + desired_name + create_part_number(num_digits, count) + '.' + target_ext
                    print(new_name)
                elif range_name is None:
                    new_name = desired_name + create_part_number(num_digits, count) + '.' + target_ext
                    print(new_name)
                # Path(obj).rename(f'{link_dir}/{new_name}')
                count += 1
    # folder = Path().cwd()
    # dir_list = Path(folder)
    # for obj in dir_list.iterdir():
    #     if obj.is_file():
    #         if str(obj).rpartition('.')[2] == source_ext:
    #             new_name = desired_name + create_part_number(num_digits, count) + '.' + target_ext
    #             print(new_name)
    #             Path(obj).rename(f'{folder}/{new_name}')
    #             count += 1

# rename_files(desired_name="new_file_", num_digits=2, source_ext="json", target_ext="txt", range_name=[1, 5])


dir_list = os.listdir('test_folder')
for obj in dir_list:
    print(f'{os.path.isdir(obj) = }', end='\t')
    print(f'{os.path.isfile(obj) = }', end='\t')
    print(f'{os.path.islink(obj) = }', end='\t')
    print(f'{obj = }')


