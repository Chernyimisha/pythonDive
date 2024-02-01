# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где ключ - тип элемента,
# а значение - список элементов данного типа.

elements = (1, 'aerf', [1, 5], {'a': 1, 'b': 2}, 2.58, (3, 6, 8), 5, 'asd', 8)
res_dict = {}

for i in elements:
    res_dict.setdefault(type(i), [])
    res_dict[type(i)].append(i)
print(res_dict)
