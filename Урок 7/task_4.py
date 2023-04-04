'''
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку
конструктора класса (метод init()), который должен принимать
данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str()
для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
'''


class Matrix():

    def __init__(self, value: list) -> None:
        self._value = value

    def __str__(self) -> str:
        str_value = ""
        for row in self._value:
            for element in row:
                str_value += str(element) + " "
            str_value += '\n'
        return str_value

    def __add__(self, other):
        if not isinstance(other, Matrix):
            return

        n = len(self._value)

        matrix = [map(sum, zip(self._value[i], other._value[i]))
                  for i in range(n)]

        return Matrix(matrix)


matrixA = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrixA)

matrixB = Matrix([[7, 8, 9], [4, 5, 6], [1, 2, 3]])
print(matrixB)

matrixC = matrixA + matrixB
print(matrixC)
