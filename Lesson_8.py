"""Задача №1"""


class Data:
    def __init__(self, day_month_year):

        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Допустимое значение'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('21 - 1 - 2021')
print(today)
print(Data.valid(21, 1, 2022))
print(today.valid(21, 13, 2021))
print(Data.extract('3 - 9 - 1988'))
print(today.extract('21 - 1 - 2021'))
print(Data.valid(21, 1, 2021))

"""Задача №2"""


class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = DivisionByNull(45, 28)
print(DivisionByNull.divide_by_null(44, 0))
print(DivisionByNull.divide_by_null(15, 0.2))
print(div.divide_by_null(45, 0))

"""Задача №3"""


class NotNumber(ValueError):
    pass


my_list = []
while True:
    try:
        value = input('Введите число в список:')
        if value == 'stop':
            break
        if not value.isdigit():
            raise NotNumber(value)
        my_list.append(int(value))
    except NotNumber as ex:
        print('Не число!', ex)
print(my_list)

"""Задача №7"""


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.с = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма с1 и с2 равна')
        return f'с = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение с1 и с2 равно')
        return f'с = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'с = {self.a} + {self.b} * i'


с_1 = ComplexNumber(7, 24)
с_2 = ComplexNumber(3, -2)
print(с_1)
print(с_1 + с_2)
print(с_1 * с_2)

"""Задачи №№4,5,6"""


class Warehouse:

    def __init__(self, producer, color, quantity):
        self.producer = producer
        self.color = color
        self.quantity = quantity


class Printer(Warehouse):

    def __init__(self, producer, color, quantity, pr_type):
        super().__init__(producer, color, quantity)
        self.pr_type = pr_type

    @staticmethod
    def name():
        print("<<Принтер>>", end=' ')

    def type_printer(self):
        return self.pr_type


class Scanner(Warehouse):

    def __init__(self, producer, color, quantity, sc_sensor):
        super().__init__(producer, color, quantity)
        self.sc_sensor = sc_sensor

    @staticmethod
    def name():
        print("<<Сканер>>", end='  ')

    def type_sensor(self):
        return self.sc_sensor


class Xerox(Warehouse):

    def __init__(self, producer, color, quantity, xer_color):
        super().__init__(producer, color, quantity)
        self.xer_color = xer_color

    @staticmethod
    def name():
        print("<<Ксерокс>>", end=' ')

    def type_color(self):
        return self.type_color


print("\n")
p = Printer('Canon', 'white', '20', 'струйный')
p.name()
print("\tпроизводитель:", p.producer, "\tцвет:", p.color, "\tколичество:", p.quantity, "\tтип принтера: ",
      p.type_printer())

s = Scanner('HP', 'black', '14', 'цветной')
s.name()
print("\tпроизводитель:", s.producer, "\tцвет:", s.color, "\tколичество:", s.quantity, "\tпримечание: ",
      s.type_sensor())

x = Xerox('Hanp', 'white', '5', 'цветной')
x.name()
print("\tпроизводитель:", x.producer, "\tцвет:", x.color, "\tколичество:", x.quantity, "\tпримечание: ", x.type_color())

"""В данной задаче осилил общую структуру, не реализовал ввод данных."""
