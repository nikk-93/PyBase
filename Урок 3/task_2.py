'''
2. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
'''

from io_func import get_int


def div_func(a, b):
    return a / b


divisible = get_int("Введите делимое")
divisor = get_int("Введите делитель")

try:
    print(div_func(divisible, divisor))
except ZeroDivisionError:
    print("Деление на ноль")
