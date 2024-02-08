# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Пример использования.
# На входе:
# file_path = "C:/Users/User/Documents/example.txt"
# На выходе:
# ('C:/Users/User/Documents/', 'example', '.txt')

# file_path = "C:/Users/User/Documents/exam.ple.txt"


def get_file_info(**link) -> tuple:
    a = link['file_path'][:link['file_path'].rfind('/') + 1]
    b = link['file_path'][link['file_path'].rfind('/') + 1:][:-len(link['file_path'][link['file_path'].rfind('.'):])]
    c = link['file_path'][link['file_path'].rfind('.'):]
    return a, b, c


print(get_file_info(file_path="C:/Users/User/Documents/exam.ple.txt"))
