from random import randint

MAX_COUNT = 8


def is_attacking(q1, q2):
    x = q1[0]
    y = q1[1]
    for i in range(1, MAX_COUNT + 1):
        if ((x, i) == q2 or (i, y) == q2 or (x + i, y + i) == q2 or (x - i, y - i) == q2
                or (x + i, y - i) == q2 or (x - i, y + i) == q2):
            return False
    return True


def check_queens(**queens):
    set_size = len(queens['queens'])
    list_set = queens['queens']
    for i in range(0, set_size):
        for j in range(0, set_size):
            if i != j and is_attacking(list_set[i], list_set[j]) is False:
                return False
    return True


print(check_queens(queens=[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)]))

# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
#
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей
# на шахматной доске, в которой ни один ферзь не бьет другого. Другими словами, ферзи размещены
# таким образом, что они не находятся на одной вертикали, горизонтали или диагонали.
#
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.
# Пример:
# [[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)],
#  [(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)],
#  [(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)],
#  [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]]


def generate_boards():
    board_list = []

    while len(board_list) < 4:
        set_list = []
        while len(set_list) == 0:
            set_list = [(i, randint(1, 8)) for i in range(1, 9)]
            if check_queens(queens=set_list) is False:
                set_list.clear()
            else:
                board_list.append(set_list)
        print(board_list)
    return board_list

print(generate_boards())

# from random import randint
#
#
# NUMBER_CONSTELLATIONS = 4
# NUMBER_QUEENS = 8
#
#
# def are_queens_attacking_each_other(queens: list(tuple())):
#     for i in range(len(queens)):
#         for j in range(i+1, len(queens)):
#             if queens[i][0] == queens[j][0] or \
#                queens[i][1] == queens[j][1] or \
#                abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
#                return False
#     return True
#
#
# def position_generation() -> list:
#     result = []
#     queens = []
#     count = 0
#
#     while count != NUMBER_CONSTELLATIONS:
#         for _ in range(NUMBER_QUEENS):
#             queens.append((randint(1,8), randint(1,8)))
#         if are_queens_attacking_each_other(queens):
#             result.append(queens)
#             count += 1
#         queens = []
#
#     return result
#
# if __name__ == '__main__':
#     for i, value in enumerate(position_generation(), 1):
#         print(f'{i} - {value}')

