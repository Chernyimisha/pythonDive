# Создайте класс МояСтрока где будут доступны все возможности str и
# дополнительно хранится имя автора строки и время создания (time.time)
from datetime import datetime


class MyStr(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        # instance.value = value
        instance.author = author
        instance.time = datetime.now()
        return instance

    def __repr__(self):
        return f"MyStr('{super().__str__()}', '{self.author}')"

    def __str__(self):
        return f'{super().__str__()} (Автор: {self.author}, Время создания: {str(self.time)[:-10]})'


event = MyStr("Завершилось тестирование", "John")
print(event)
print(repr(event))



# class NamedInt(int):
#     def __new__(cls, value, name):
#         instance = super().__new__(cls, value)
#         instance.name = name
#         print(f'Создал класс {cls}')
#         return instance
#
#
# print('Создаём первый раз')
# a = NamedInt(42, 'Главный ответ жизни, Вселенной и вообще')
# print('Создаём второй раз')
# b = NamedInt(73, 'Лучшее просто число')
# print(f'{a = }\t{a.name = }\t{type(a) = }')
# print(f'{b = }\t{b.name = }\t{type(b) = }')
# c = a + b
# print(f'{c = }\t{type(c) = }')


