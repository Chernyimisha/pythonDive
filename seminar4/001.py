# my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
# # s_key = sorted(my_dict.items())
# s_key = sorted(my_dict.keys())
# s_value = sorted(my_dict.items(), key=lambda x: x[0], reverse=True)
# print(f'{s_key = }\n{s_value = }')

# Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировки Unicode
# Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки

text = 'Пользователь вводит строку текста. Вывести каждое слово с новой строки.'


def new_output(line: str):

    """
    fefafadfasdfasdfadsfadsfasdf
    :param line: str
    :return: output string
    >>> new_output('Пользователь вводит строку текста. Вывести каждое слово с новой строки.')
    1       вводит
    2      вывести
    3       каждое
    4        новой
    5 пользователь
    6            с
    7        слово
    8      строки.
    9       строку
    10      текста.
    """
    line_split = line.lower().split()
    line_split.sort()
    max_indentation = len(max(line_split, key=len))
    for i in line_split:
        if len(i) > max_indentation:
            max_indentation = len(i)
    for i, line in enumerate(line_split, 1):
        print(f'{i} {line:>{max_indentation}}')


new_output(text)
