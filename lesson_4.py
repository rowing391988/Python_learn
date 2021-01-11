# Задача №1

from sys import argv


def payday():
    try:
        hour, rate, bonus = map(float, argv[1:])
        print(f"payday - {hour * rate + bonus}")
    except ValueError:
        print("Введите значения ввиде чисел")


payday()

# Задача №2

old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [old_list[i] for i in range(1, len(old_list)) if old_list[i] > old_list[i - 1]]
print(new_list)

"""old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []
for i in range(1, len(old_list)):
    if old_list[i] > old_list[i - 1]:
        new_list.append(old_list[i])
        print(new_list)"""
# Задача №3

new_list = [i for i in range(1, 240) if i % 20 == 0 or i % 21 == 0]
print(new_list)

# Задача №4
from random import randint

old_list = [randint(-10, 10) for n in range(20)]
new_list = [i for i in old_list if old_list.count(i) == 1]
print(f"old_list {old_list}\n new_list {new_list}")

# Задача №5
from functools import reduce


def my_list(i_1, i_2):
    return i_1 * i_2


new_list = [i for i in range(100, 1001) if i % 2 == 0]
print(f"список четных чисел от 100 до 1000:\n {new_list}\n произведение этих чисел:\n {reduce(my_list, new_list)}")

# Задача №6 ( Прорешал после разбора Д/З)
from itertools import count, cycle

for i in count(int(input("Введите стартовое число: "))):
    print(i, end='')
    quit = input()
    if quit == "q":
        break

new_list = input("Введите значения через пробел: ").split()
iter = cycle(new_list)
quit = None
while quit != 'q':
    print(next(iter), end='')
    quit = input()


# Задача №7 ( Прорешал после разбора Д/З)
def my_fact(num):
    f_num = 1
    if num == 0:
        yield f"{num}! = 1"
    for i in range(1, num + 1):
        f_num *= i
        yield f"{i}! = {f_num}"


for el in my_fact(int(input("факториал числа: "))):
    print(el)
