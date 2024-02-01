# Задание №7
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

line = 'Пользователь вводит строку текста. Вывести каждое слово с новой строки.'
res_dict = {}
# c методом count
# line_set = set(line)
# for el in line_set:
#     counter = line.count(el)
#     res_dict.setdefault(el)
#     res_dict[el] = counter
# print(res_dict)

# без метода count
# for el in line_set:
#     counter = 0
#     for i in line:
#         if i == el:
#             counter += 1
#     res_dict.setdefault(el)
#     res_dict[el] = counter
# print(res_dict)

# решение участников семинара

for el in line:
    res_dict[el] = res_dict.get(el, 0) + 1
print(res_dict)

