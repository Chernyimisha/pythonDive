# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е. Точность вычислений должна составлять не менее 42 знаков после запятой.

import decimal

decimal.getcontext().prec = 42
diameter = float(input('Введите диаметр окружности: '))

radius = decimal.Decimal(diameter / 2)
PI = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
area = PI * radius**2
lenght = 2 * PI * radius

print(area, lenght, sep='\n')