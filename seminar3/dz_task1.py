ruc = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0
# weight = 0
# backpack = {}
#
# for key in items:
#
#     if weight < max_weight:
#         backpack[key] = items.get(key)
#         weight += items.get(key)
#         print(weight)
#
backpack = {}
for item, weight in ruc.items():
    if weight <= max_weight:
        backpack[item] = weight
        max_weight -= weight
print(backpack)