# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое
# или вещественное число. Обрабатывайте не числовые данные как исключения.

def getnumber():
    while True:
        try:
            number = float(input("Введите число: "))
            return number
        except ValueError:
            print("Введено не число")


numb = getnumber()
print(f'Вы ввели: {numb}')

