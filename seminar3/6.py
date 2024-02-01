# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировке Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

line = 'Пользователь вводит строку текста. Вывести каждое слово с новой строки.'
line_split = line.lower().split()
line_split.sort()
max_indentation = len(max(line_split, key=len))
for i in line_split:
    if len(i) > max_indentation:
        max_indentation = len(i)
for i, line in enumerate(line_split, 1):
    print(f'{i} {line:>{max_indentation}}')
