# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого символа
# введённой строки отсортированный по убыванию.

text = 'Generate UNICODE text'


def generate_unicode(txt: str) -> list[int]:
    result = []
    for char in txt:
        result.append(ord(char))
    return sorted(set(result), reverse=True)


print(generate_unicode(text))
