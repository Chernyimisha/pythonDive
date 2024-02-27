# Создайте класс Архив, который хранит пару свойств. Например, число и строку. При нового экземпляра класса,
# старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов, которые также являются
# свойствами экземпляра.


class Archive:

    _instance = None

    def __new__(cls, text, number):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
            cls._instance.archive_text.append(text)
            cls._instance.archive_number.append(number)
        else:
            cls._instance.archive_text.append(text)
            cls._instance.archive_number.append(number)
        return cls._instance

    def __init__(self, text: str, number: int | float):
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Data_("{self.text}", {self.number})'


if __name__ == '__main__':
    #     c = Data_('Hello', 'Jo')
    #     b = Data_('Good', 'Gregory')
    #     d = Data_('sdf', 'sdf')
    # #     print(Data_.__dict__)
    # #
    # # print(f"{c = }\t{c.all_text = }\t{c.all_name = }\t{type(c)}")
    # # print(f"{b = }\t{b.all_text = }\t{b.all_name = }\t{type(b)}")
    # # print(f"{d = }\t{d.all_text = }\t{d.all_name = }\t{type(d)}")
    #     print(repr(d))
    archive1 = Archive("Запись 1", 42)
    archive2 = Archive("Запись 2", 3.14)
    archive3 = Archive("Запись 3", 5.14)
    # print(repr(archive1))
    print(archive2)
    print(archive1.archive_text)
    print(archive1.archive_number)

