import random


# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.


VOWELS = 'AEIOU'
CONSONANTS = 'BCDFGHJKLMNPQRSTVWXYZ'


def _name_generator():
    return ''.join([random.choice(CONSONANTS) if i % 2 != 0 else random.choice(VOWELS)
                    for i in range(random.randint(4, 7))]).capitalize()


def pseudo_names(quantity: int, filename: str):
    with open(filename, 'w') as f:
        # for i in range(quantity):
        #     print(f'{_name_generator()}', file=f)
        f.writelines([_name_generator() + '\n' for _ in range(quantity)])


pseudo_names(5, 'words.txt')


def my_readline(file):
    line = file.readline()
    if line == '':
        file.seek(0)
        return file.readline()
    return line


def write_with_join(names, numbers, result_names) -> None:
    with (open(names, 'r') as name, open(numbers, 'r') as numb,
          open(result_names, 'w') as res):
        len_name = len(name.read().split('\n'))
        len_namb = len(numb.read().split('\n'))
        max_len = max(len_namb, len_name)

        for i in range(max_len - 1):
            new_name = my_readline(name).replace('\n', '')
            new_int, new_float = my_readline(numb).replace('\n', '').split('|')
            new_numb = int(new_int) * float(new_float)
            if new_numb < 0:
                res.write(f'{new_name.lower()} {abs(new_numb)}\n')
            else:
                res.write(f'{new_name.upper()} {int(new_numb)}\n')

write_with_join('words.txt', 'numbers.txt', 'result.txt')


