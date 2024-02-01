# Вручную создайте список с целыми числами, которые повторяются.
# Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
# *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков

numbers = [4, 4, 5, 9, 7, 1, 2, 5]

new_list = list(set(numbers))
print(new_list)
print(type(new_list))

new_list_1 = []

for i in numbers:
    if i not in new_list_1:
        new_list_1.append(i)

new_list_1.sort()

print(new_list_1)