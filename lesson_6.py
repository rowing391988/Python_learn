# Задача #1
import time


class TrafficLight:
    __color = ['Красный', 'Желый', 'Зеленый']

    def running(self):
        self.__color = 'Красный'
        print(f'Цвет: {self.__color}')
        time.sleep(7)

        self.__color = 'Желтый'
        print(f'Цвет: {self.__color}')
        time.sleep(2)

        self.__color = 'Зеленый'
        print(f'Цвет: {self.__color}')
        time.sleep(3)

        while True:
            self.running()


light = TrafficLight()
print(light.running())


# Задача №2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def mass(self):
        mass = self._length * self._width * self.weight * self.height / 1000
        print(f"Масса асфальта = {round(mass)} т")


a = Road(30, 1000)
a.mass()



# Задача №3
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def full_name(self):
        return self.name + ' ' + self.surname

    def ful_income(self):
        return self._income["wage"] + self._income["bonus"]


a = Position('Ivan', 'Ivanov', 'Manager', '100000', '50000')
print(a.full_name(), a.ful_income())



# Задача №4
class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала.'

    def stop(self):
        return f'\nМашина {self.name} остановилась.'

    def turn(self, direction):
        return f'\nМашина {self.name} повернула {direction}'

    def show_speed(self):
        return f'\nВаша скорость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nПривышение скорости!!! Ваша скорость {self.speed}'
        else:
            return f'Скрость {self.name} разрешенная'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nПривышение скорости!!! Ваша скорость {self.speed}'
        else:
            return f'Скрость {self.name} разрешенная'


class PoliceCar(Car):
    pass


town = TownCar('LADA', 70, 'Белая', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('направо'), town.turn('налево'), town.stop())

sport = SportCar('ZAZ', 170, 'Синий', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('направо'), sport.stop())

work = WorkCar('BMW', 30, 'Красный', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar('Kia', 100, 'Черный', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('налево'), work.stop())


# Задача №5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашем')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())
