# На семинаре про декораторы был создан логирующих декоратор. Он сохранял аргументы функции и результат её
# работы в файл. Напишите аналогичный декоратор, но внутри используйте модуль logging.


import logging


def log_decorator(func):

    def wrapper(*args, **kwargs):

        logging.basicConfig(filename=f'{func.__name__}.log', encoding='utf-8', level=logging.NOTSET)
        res = func(*args, **kwargs)
        logging.debug(f'{args} {kwargs} {res}')
        return res

    return wrapper


@log_decorator
def division(x: (int, float), y: (int, float)):
    try:
        return x / y
    except ZeroDivisionError as err:
        return float('inf')


if __name__ == '__main__':
    division(2, 5)