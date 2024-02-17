
import random


# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

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