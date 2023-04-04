'''
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет)
и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета используйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''

from time import sleep


class TrafficLight():

    def __init__(self, colors_timer: dict) -> None:
        self.__colors_timer = colors_timer
        self.__colors_key = list(colors_timer.keys())
        self.__step = 1
        self.__current = -1

    def __next_color(self):
        self.__current += self.__step

        if self.__current == len(self.__colors_key) - 1:
            self.__step = -1
        elif self.__current == 0:
            self.__step = 1

    def __display(self):
        print(self.__colors_key[self.__current])

    def __sleep_color(self):
        color = self.__colors_key[self.__current]
        sleep(self.__colors_timer[color])

    def running(self, count_step=-1):
        i = 0
        while True:
            i += 1
            if count_step != -1 and i > count_step:
                break
            self.__next_color()
            self.__display()
            self.__sleep_color()


traffic_light = TrafficLight({"красный": 7, "желтый": 2, "зеленый": 5})
traffic_light.running()
