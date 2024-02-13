# Создайте генератор чётных чисел от нуля до 100.
# Из последовательности исключите числа, сумма цифр которых равна 8. Решение в одну строку.
from random import randint


list_0 = [i for i in range(0, 101, 2) if sum(map(int, str(i))) != 8]

# list_0 = [(i, randint(1, 8)) for i in range(1, 9)]


print(list_0)

