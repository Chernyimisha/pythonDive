from collections import namedtuple
from datetime import datetime
import time
import argparse
import os
from pathlib import Path


# User = namedtuple('User', ['first_name', 'last_name', 'birthday'])
# u_1 = User('Исаак', 'Ньютон', datetime(1643, 1, 4))
# print(u_1)
# print(f'{type(User)}, {type(u_1)}')
#
# User2 = namedtuple('User', ['first_name', 'last_name', 'birthday'], defaults=['Иванов', datetime.now()])
# u_2 = User2('Исаак')
# print(f'{u_1.last_name}, {u_1.birthday.strftime("%H:%M:%S")}')
# time.sleep(7)
# u_3 = User2('Галилей', 'Галилео')
# print(f'{u_3.last_name}, {u_3.birthday.strftime("%H:%M:%S")}')
#
# Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
# a = Point(2, 3, 4)
# b = a._replace(z=0, x=a.x + 4)
# print(a)

# Point2 = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
# data = [Point2(2, 3, 4), Point(10, -100, -500), Point(3, 7, 11), Point2(2, 202, 1)]
# print(sorted(data))


# parser = argparse.ArgumentParser(description='My first argument parser')
# parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
# args = parser.parse_args()
# print(f'В скрипт передано: {args}')

os.mkdir('test_folder')
for i in range(5):
    dir_name = f'test_folder/test_folder{i}'
    os.mkdir(dir_name)
    for j in range(5):
        file_name = f'{dir_name}/test_file{j}.txt'
        with open(file_name, 'w') as f:
            pass


