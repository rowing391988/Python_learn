"""Задача №1"""


class Matrix:

    def __init__(self, rows):
        self.rows = list(rows)

    def __str__(self):
        string = ''
        for row in self.rows:
            for idx, el in enumerate(row, start=1):
                string += str(el)
                if idx < len(row):
                    string += ' '
                else:
                    string += '\n'
        return string

    def __add__(self, other):
        result = Matrix([])
        for row_a, row_b in zip(self.rows, other.rows):
            result.rows.append([i + j for i, j in zip(row_a, row_b)])
        return result


A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(A + B)

"""Задача №2"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, growth):
        self.growth = growth

    @property
    def consumption(self):
        return 2 * self.growth + 0.3


a = Coat(110)
b = Suit(50)

print(f'Расход ткани на пальто: {a.consumption:.2f}')
print(f'Расход ткани на костюм: {b.consumption:.2f}')

"""Задача №3"""


class Cell:
    def __init__(self, count):
        self.count = count

    def __str__(self):
        return str(self.count)

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        return abs(self.count - other.count)

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return self.count // other.count

    def make_order(self, row):
        return ('\n'.join(['*' * row for _ in range(self.count // row)]) + '\n') + ('*' * (self.count % row))


a = Cell(14)
b = Cell(7)

print(f"a = {a}")
print(f"b = {b}")
print('-' * 100)

print(f"a + b = {Cell(a + b)}")
print(f"a - b = {Cell(a - b)}")
print(f"a * b = {Cell(a * b)}")
print(f"a / b = {Cell(a / b)}")

print('-' * 100)

print(a.make_order(4))
