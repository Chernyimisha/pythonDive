from typing import Union


class MyError(Exception):
    pass


class InvalidTextError(MyError):
    pass


class InvalidNumberError(MyError):
    pass


def validator_text(value):
    if not isinstance(value, str) or value == '':
        raise InvalidTextError(f'Invalid text: {value}. Text should be a non-empty string.')


def validator_number(value):
    if not isinstance(value, (int, float)) or value <= 0:
        raise InvalidNumberError(f'Invalid number: {value}. Number should be a positive integer or float.')


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        validator_text(text)
        validator_number(number)
        self.text = text
        self.number = number

    def __setattr__(self, key, value):
        if key == 'text':
            validator_text(value)
        elif key == 'number':
            validator_number(value)
        object.__setattr__(self, key, value)

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


a = Archive(5, 5)
print(a)

