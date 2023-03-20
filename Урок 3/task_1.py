'''
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
'''

import math

from io_func import get_int

month_per_season = 3
season_name_dict = {0: "Winter", 1: "Spring", 2: "Summer", 3: "Autumn"}
season_name_list = ["Winter", "Spring", "Summer", "Autumn"]

month_num = get_int("Введите месяц")
month_shift_num = month_num + 1 if month_num < 12 else 1
season_index = math.ceil(month_shift_num / month_per_season) - 1

print(season_name_dict[season_index])
print(season_name_list[season_index])
