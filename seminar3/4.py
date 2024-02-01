# Создайте вручную список с повторяющимися элементами. Удалите из него все элементы, которые встречаются дважды.

elements = [1, 'aerf', [1, 5], {'a': 1, 'b': 2}, 2.58, (3, 6, 8), 5, 'asd', 8, 5, 'asd', 1, 2, 'r', 2.58]
# elements = [1, 5, 2, 3, 4, 9, 7, 6, 8, 4, 2, 3, 6, 7, 4, 5, 4]

for i in elements:
# for i in set(elements):
    counter = elements.count(i)
    if counter > 1:
        for _ in range(counter):
            elements.remove(i)

print(elements)
