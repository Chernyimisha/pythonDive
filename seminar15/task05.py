# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить.
# В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое названия дня недели и месяца,
# но и числовые, т.е не мая, а 5
import argparse

from seminar15.task04 import string_to_date, MONTHS, DAYS


def cl_parser():
    parser = argparse.ArgumentParser(description='String to date')
    parser.add_argument('-w', '--weeks', default='1')
    parser.add_argument('-wd', '--weekdays', default='понедельник')
    parser.add_argument('-m', '--months', default='января')
    args = parser.parse_args()
    weekdays = args.weekdays if not args.weekdays.isdigit() else DAYS[int(args.weekdays) - 1]
    months = args.months if not args.months.isdigit() else MONTHS[int(args.months) - 1]
    return string_to_date(f'{args.weeks} {weekdays} {months}')


if __name__ == '__main__':
    cl_parser()