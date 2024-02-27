
class LotteryGame:
    def __init__(self, list1: list, list2: list):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        result = []
        for i in self.list1:
            for j in self.list2:
                if i == j:
                    result.append(i)
                    break
        if len(result) != 0:
            result_print = f'Совпадающие числа: {result}\nКоличество совпадающих чисел: {len(result)}'
        else:
            result_print = 'Совпадающих чисел нет.'

        print(result_print)

if __name__ == "__main__":
    # list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
    # list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]
    list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    game = LotteryGame(list1, list2)

    game.compare_lists()

