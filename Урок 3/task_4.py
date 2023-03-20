'''
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
'''

from random import randint


def get_rand_numbers(count, low_value, high_value):
    return [randint(low_value, high_value) for i in range(count)]


def sort_descending(*args):
    list_number = list(args)
    list_number.sort(reverse=True)
    return list_number


def get_sum_with_sort(numbers, count_elements_sum):
    # Можно использовать heapq.nlargest(n, iterable, key=None)
    numbers_to_sum = sort_descending(*numbers)[:count_elements_sum]
    return sum(numbers_to_sum), numbers_to_sum


def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] <= a[j+1]:
                continue
            a[j], a[j+1] = a[j+1], a[j]
    return a


def get_max_numbers(count, *args):
    return bubble_sort(list(args))[-count:]


def get_sum_wout_sort(numbers, count_elements_sum):
    numbers_to_sum = get_max_numbers(count_elements_sum, *numbers)
    return sum(numbers_to_sum), numbers_to_sum


numbers = get_rand_numbers(10, 1, 10)
count_elements_sum = 3
print(numbers)
print(get_sum_with_sort(numbers, count_elements_sum))
print(get_sum_wout_sort(numbers, count_elements_sum))
