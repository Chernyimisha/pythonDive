# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно

# number = 10
# number_two = number
# res = ''
# while number != 0:
#     res = str(number % 2) + res
#     number //= 2
# print(f'0b{res}')
# print(bin(number_two))
#
# number = 10
# number_two = number
# res = ''
# while number != 0:
#     res = str(number % 8) + res
#     number //= 8
# print(f'0o{res}')
# print(oct(number_two))

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
num = 0
number_two = num
res = ''
while num != 0:
    res = numbers[num % 16] + res
    num //= 16
print(f'Шестнадцатеричное представление числа: {res}')
print(f'Проверка результата: {hex(number_two)}')

# Шестнадцатеричное представление числа: FF
# Проверка результата: 0xff
