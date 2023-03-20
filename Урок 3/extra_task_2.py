'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий
по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число
N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
'''

from io_func import get_int
import sys


def get_close_values(numbers, x):
    min_delta = sys.maxsize
    close_values = []
    for number in numbers:
        delta = abs(x - number)
        if min_delta < delta:
            continue
        if min_delta == delta:
            close_values.append(number)
            continue
        min_delta = delta
        close_values = [number]
    return set(close_values)


n = get_int("Введите кол-во элементов")
numbers = [get_int(f"Введите {i + 1}-е число") for i in range(n)]
print(numbers)
x = get_int("Введите искомое число")
print(f"Самые близкие элементы: {get_close_values(numbers, x)}")
