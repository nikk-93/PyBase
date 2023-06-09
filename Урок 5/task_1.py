'''
Задание 1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
'''

import operator
import os
from io_func import get_int, repeatOnError


def get_operator(text):
    operators = {'+': operator.add, '-': operator.sub,
                 '*': operator.mul, '/': operator.truediv}
    result = operators.get(text, None)
    if result:
        return result
    else:
        raise ValueError(f"Допустимы операторы: {list(operators.keys())}")


@repeatOnError(ValueError)
def input_operator():
    text = input("Введите оператор: ")
    if text == '0':
        return None
    else:
        return get_operator(text)


def check_input(n, m, func):
    if func == operator.truediv and m == 0:
        print("Нельзя делить на ноль")
        return False
    else:
        return True


def exec_func():
    os.system('cls')
    func = input_operator()
    if not func:
        return
    n = get_int("Введите первое число")
    m = get_int("Введите второе число")
    if check_input(n, m, func):
        print(f"Результат: {func(n, m)}")
    input("Нажмите любую клавишу для продолжения...")
    exec_func()


exec_func()
