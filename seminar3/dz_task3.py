# Дан список повторяющихся элементов lst.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

lst = [1, 1, 2, 2, 3, 3]
result = []
for i in lst:
    if lst.count(i) > 1:
        if i not in result:
            result.append(i)
print(result)
