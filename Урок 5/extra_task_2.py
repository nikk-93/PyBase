'''
Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.

*Пример:*

2 2
    4
'''

from io_func import get_int


def sum_number(a, b):
    if a <= 0 and b <= 0:
        return 0
    elif a <= 0:
        return 1 + sum_number(0, b - 1)
    elif b <= 0:
        return 1 + sum_number(a - 1, 0)
    else:
        return 1 + 1 + sum_number(a - 1, b - 1)


n = get_int("Введите первое число")
m = get_int("Введите второе число")

print(sum_number(n, m))
