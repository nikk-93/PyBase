'''
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income).

Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике
также через перегрузку str
str(self) - вызывается функциями str, print и format.
Возвращает строковое представление объекта.
'''


class Worker():
    def __init__(self) -> None:
        self.name = ''
        self.surname = ''
        self.position = ''
        self._income = {"wage": 0, "bonus": 0}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus) -> None:
        super().__init__()
        self.name = name
        self.surname = surname
        self.position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def __str__(self) -> str:
        return (f"Сотрудник {self.get_full_name()}, "
                f"доход {self.get_total_income()}, "
                f"должность {self.position}")


position = Position("Nikita", "Ladygin", "Developer", 100, 100)

print(position)
