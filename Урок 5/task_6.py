'''
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
'''

from random import randint
from io_func import get_int


def game(number, try_count):
    if try_count <= 0:
        print(f"Попытки исчерпаны, загаданное число: {number}")
        return

    try_number = get_int("Отгадай число")

    if try_number == number:
        print("Бинго!")
        return

    if try_number < number:
        print("Введенное число меньше загаданного")
    else:
        print("Введенное число больше загаданного")

    game(number, try_count - 1)


number = randint(0, 101)
game(number, 10)
