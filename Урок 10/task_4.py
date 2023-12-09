"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


def print_double_convert(text: str):
    text_bytes = text.encode(encoding='utf-8')
    print(text_bytes)
    print(text_bytes.decode(encoding='utf-8'))
    print()


print_double_convert('разработка')
print_double_convert('администрирование')
print_double_convert('protocol')
print_double_convert('standard')
