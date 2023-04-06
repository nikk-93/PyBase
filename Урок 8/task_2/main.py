"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json
import inspect
import os
import sys
from datetime import date


def get_script_dir(follow_symlinks=True) -> str:
    if getattr(sys, 'frozen', False):  # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


def read_order_from_json(path_file: str):
    try:
        with open(path_file, 'r') as f_r:
            obj = json.load(f_r)
            return obj
    except Exception:
        return {'orders': []}


def write_order_to_json(item, quantity, price, buyer, date, path_file: str):
    dict_orders = read_order_from_json(path_file)
    dict_to_json = {'item': item,
                    'quantity': quantity,
                    'price': price,
                    'buyer': buyer,
                    'date': date}
    dict_orders['orders'].append(dict_to_json)
    with open(path_file, 'w') as f_a:
        json.dump(dict_orders, f_a, indent=4)


write_order_to_json('PC', 123, 432, 'I', date.today().strftime('%d.%m.%Y'),
                    os.path.join(get_script_dir(), 'my_orders.json'))
