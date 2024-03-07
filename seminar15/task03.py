# Доработаем задачу 2. Сохраняйте в лог файл раздельно: уровень логирования, дату события,
# имя функции (не декоратора), аргументы вызова, результат.


import logging
from functools import wraps

FORMAT = '{levelname:<8} - {asctime}. В функции {funcName} {msg}'
logging.basicConfig(format=FORMAT, filename='Task_3.log', encoding='utf-8', style='{', level=logging.NOTSET)


def log_decorator(func):
    logger = logging.getLogger(__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        logger.debug(f'{func.__name__} {args} {kwargs} {res}')
        logger.debug(f'{args} {kwargs} {res}')
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