# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if. Попробуйте разные значения e и n.

n = int(input())
e = int(input())
count = 0

for i in range(2, n + 1, 2):
    if i % e != 0:
        count += i

print (count)
