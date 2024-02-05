# Функция получает на вход список чисел и два индекса. Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
# Если нижняя граница меньше нуля, суммируем от начала. Если верхняя граница больше длины списка, до конца.


data = {
    "Рога": [42, -73, 12, 85, -15, 2],
    "Копыта": [45, 25, -100, 22, 1],
    "Хвосты": [-500, 123, 52, 45, 93],
}


def is_all_profit(dct: dict) -> bool:
    return all(map(lambda v: sum(v) > 0, dct.values()))


print(is_all_profit(data))

print(list(map(lambda v: sum(v) > 0, data.values())))