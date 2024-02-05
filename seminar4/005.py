# Функция принимает на вход три списка одинаковой длины: имена str, ставка int, премия str
# с указанием процентов вида “10.25%”. Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

def fn(names: list[str], salary: list[int], bonus: list[str]) -> dict:
    res = {}
    for name, salary, bonus in zip(names, salary, bonus):
        res[name] = round(salary * float(bonus.replace("%", ""))/100, 2)
    return res


lst_1 = ['don', 'mic', 'susan']
lst_2 = [1000, 2000, 10000]
lst_3 = ['5.2%', '1.2%', '6.9%']

print(fn(lst_1, lst_2, lst_3))