"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml
import inspect
import os
import sys


def get_script_dir(follow_symlinks=True) -> str:
    if getattr(sys, 'frozen', False):  # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


def load_yaml(path_file: str):
    with open(path_file, 'r') as f_r:
        return yaml.load(f_r, Loader=yaml.FullLoader)


def dump_yaml(data, path_file: str):
    with open(path_file, 'w') as f_w:
        yaml.dump(data, f_w, default_flow_style=False, allow_unicode=True)


data_dict = {"key_1": ['item_1', 'item_2'],
             "key_2": 123,
             "key_3": {'computer': '200€-1000€'}}

print(data_dict)
dump_yaml(data_dict, os.path.join(get_script_dir(), 'my_file.yaml'))
data_dict = load_yaml(os.path.join(get_script_dir(), 'my_file.yaml'))
print(data_dict)
