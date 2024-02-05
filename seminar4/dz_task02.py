# Напишите функцию key_params, принимающую на вход только ключевые параметры и
# возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def key_params(**args):
    new_dict = {}
    for k, value in args.items():
        if value.__hash__ is None:
            value = str(value)
        new_dict[value] = k
    return new_dict


params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)