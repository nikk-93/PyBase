"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, которые нужно 
перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
"""

n = int(input("Введите количество монет: "))

zero_coin = 0
one_coin = 0

for i in range(n):
    if int(input(f"{i+1}-я монета (0 - решка 1 - орел): ")):
        one_coin += 1
    else:
        zero_coin += 1

if one_coin >= zero_coin:
    print(zero_coin)
else:
    print(one_coin)
