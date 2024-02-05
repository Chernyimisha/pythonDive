# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def create_dict(numbers_str: str) -> dict:
    str_split = numbers_str.split(' ')
    print(str_split)
    num1, num2 = map(int, str_split)
    counter = min(num1, num2)
    max_number = max(num1, num2)
    result = {}

    while counter <= max_number:
        result[chr(counter)] = counter
        counter += 1

    return result


print(create_dict('90 105'))
