"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""


def print_info_bytes(text: str):
    text_bytes = bytes(text, "utf-8")
    print(type(text_bytes), text_bytes, len(text_bytes))


print_info_bytes('class')
