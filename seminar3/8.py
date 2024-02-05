# Задание №8
# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

hike = dict(Aaz=("спички", "спальник", "дрова", "топор"),
            Skeeve=("спальник", "спички", "вода", "еда"),
            Tananda=("вода", "спички", "косметичка"))

temp_bag = None
for things in hike.values():
    if not temp_bag:
        temp_bag = set(things)
        continue
temp_bag = temp_bag.intersection(set(things))
print(temp_bag)


result_uniq = {}
for name, things in hike.items():
    temp = set(things)
    temp_o = set()
for other in hike.values():
    if things == other:
        continue
        temp_o = temp_o.union(set(other))
        temp = temp.difference(temp_o)
    if temp:
        result_uniq.update({name: temp})
print(result_uniq)


res_missing = {}
for name, things in hike.items():
    temp = set(things)
for other in hike.values():
    if things == other:
        continue
    temp_o = temp_o.intersection(set(other))
    temp = temp_o.difference(temp)
    if temp:
        res_missing.update({name: temp})
print(res_missing)
