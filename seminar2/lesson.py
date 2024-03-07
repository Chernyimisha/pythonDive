# num = int(input("Input number: "))
# print(f"Type object: {type(num)}, adress: {id(num)}, hash: {hash(num)}")

# help()

# Примеры текстов для демонстрации:
texts = ["123", "Привет", "255", "Hello", "0xFF", ""]


# Функция для проверки и преобразования текста, если это возможно, и вывода результатов

def process_text(texts):
    for text in texts:
        try:
            # Попытка преобразовать текст в целое число
            number = int(text)
            # Выводим двоичное, восьмеричное и шестнадцатеричное представления числа
            binary = bin(number)
            octal = oct(number)
            hexadecimal = hex(number)
            result = (binary, octal, hexadecimal)
        except ValueError:
            # Если преобразование не удалось, проверяем, состоит ли текст из символов ASCII
            if all(ord(char) < 128 for char in text):
                result = "Текст написан в ASCII."
            else:
                result = "Текст содержит не-ASCII символы."
        print(f"Текст: '{text}' Результат: {result}")


# Выполнение функции и вывод результатов
process_text(texts)
