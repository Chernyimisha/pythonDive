# Создайте класс-функцию, который считает факториал числа при вызове экземпляра. Экземпляр должен запоминать
# последние k значений. Параметр k передаётся при создании экземпляра. Добавьте метод для просмотра ранее
# вызываемых чисел и их факториалов.


from collections import defaultdict
import json


class Storage:
    def __init__(self):
        self.stor = defaultdict(list)

    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.stor.items()))
        return f'Объекты хранилища по типам:\n{txt}'

    def __call__(self, value):
        self.stor[type(value)].append(value)
        return f'К типу {type(value)} добавлен {value}'


class Faktorial:
    def __init__(self, size, file):
        self.storage = dict()
        self.size = size
        self.file_name = file

    def __str__(self):
        data = ' '.join((f'{k}: {v}' for k, v in self.storage.items()))
        return f'Объекты хранилища: {data}'

    def __call__(self, number):
        result = 1
        for i in range(1, number + 1):
            result *= i
        self.storage[number] = result
        if len(self.storage) > self.size:
            self.storage.pop(list(self.storage)[0])
            # for i in self.storage.keys():
            #     del self.storage[i]
            #     break
        return f'В хранилище добавлен {number} со значением {result}'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.file_name, 'w') as f:
            json.dump(self.storage, f, indent=2)
        self.storage.clear()

if __name__ == '__main__':
    s = Faktorial(5, 'storage.txt')
    with s:
        print(s(1), ' ', s)
        print(s(2), ' ', s)
        print(s(3), ' ', s)
        print(s(4), ' ', s)
        print(s(5), ' ', s)
        print(s(6), ' ', s)
        print(s(7), ' ', s)
        print(s(8), ' ', s)
        print(s(9), ' ', s)
