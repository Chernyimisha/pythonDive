# Нарисовать в консоли ёлку спросив у пользователя количество рядов. Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********


number = int(input("Введите количесвтво рядов ёлочки: "))
count = 1
for i in range(1, number * 2, 2):
    print(' ' * (number - count), '*' * i)
    count += 1

