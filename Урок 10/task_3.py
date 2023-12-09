"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки
b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""


def print_info_ascii(text: str):
    try:
        print(text, bytes(text, encoding='ASCII'))
    except UnicodeEncodeError:
        print(f"{text} невозможно преобразовать")
    print()


print_info_ascii('attribute')
print_info_ascii('класс')
print_info_ascii('функция')
print_info_ascii('type')
