"""
Задача 14: Требуется вывести все целые степени двойки 
(т.е. числа вида 2k), не превосходящие числа N.
"""

import math

n = int(input("Введите число: "))

print(math.floor(math.log(n, 2)))
