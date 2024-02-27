# Создайте класс-генератор. Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с
# шагом step. Если переданы два параметра, считаем step=1. Если передан один параметр, также считаем start=1.


class IterFator:
    def __init__(self, stop, start=1, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.start, self.stop, self.step):
            result = 1
            for j in range(1, i + 1):
                result *= j
            self.start += self.step
            return result
        raise StopIteration

if __name__ == '__main__':

    # f = IterFator(10, 2, 2)
    # for i in f:
    #     print(i)

    f = IterFator(12, 6)
    for i in f:
        print(i)

