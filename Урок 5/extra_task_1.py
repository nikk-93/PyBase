'''
Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
'''

from io_func import get_int


def power(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    elif k == -1:
        return 1 / n
    elif k > 1:
        return n * power(n, k - 1)
    elif k < -1:
        return 1 / n * power(n, k + 1)


n = get_int("Введите число")
k = get_int("Введите степень")

print(f"Результат: {power(n, k)}")
