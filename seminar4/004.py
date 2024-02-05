# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком. Её описание есть в википедии.

numbers = [2, 8, 1, 6, 8, 1, 0, 6, 99, 14, 52, 64, 4, 7]


def bubble_sort(lst: list) -> None:
    n = len(lst)
    for i in range(n):
        for j in range(n):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                print(lst)


bubble_sort(numbers)
print(numbers)