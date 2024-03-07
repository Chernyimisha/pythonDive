# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году. Логируйте ошибки, если текст не соответсвует формату.
from seminar15.task03 import log_decorator
import datetime

MONTHS = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
          'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
DAYS = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']


@log_decorator
def string_to_date(s: str) -> datetime:
    weeks, weekday, month = s.split()
    weeks = int(weeks[0])
    y = datetime.datetime.now().year
    month_num = MONTHS.index(month) + 1
    weekday = DAYS.index(weekday) + 1
    first_day = datetime.date(day=1, month=month_num, year=y).isoweekday() # 1-7
    day_by_date = ((1 + 7 * weeks - (first_day - weekday))
    if weekday < first_day else 1 + 7 * (weeks - 1) - (first_day - weekday))
    return datetime.datetime(day=day_by_date, month=month_num, year=y)


if __name__ == '__main__':
    string_to_date('1-й четверг ноября')
    string_to_date('1-е воскресенье февраля')
    string_to_date('5-й четверг февраля')
    string_to_date('5-е воскресенье марта')
    string_to_date('5-е воскресенье марта')
    string_to_date('5-е пятница мая')
