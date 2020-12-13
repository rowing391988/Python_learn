
print("Задача 1")
name = 'Андрей '
print("Привет пользователь " + name)
last_name = input('Введите вашу фамилию: ')
print(name + last_name)
age = int(input("Введите ваш возраст: "))
current_year = int(input("Введите текущий год: "))
year_of_birth = current_year - age
print('Поздравляю! Вы родились в ' + str(year_of_birth) + " году")

print("Задача 2")
second = int(input("Введите количество секунд: "))
hour = second // 3600
minute = (second - (hour * 3600)) // 60
found_second = second - (hour * 3600) - (minute * 60)
print(str(hour) + ':' + str(minute) + ':' + str(found_second))

print("Задача 3")
number_n = input("Введите произвольное число: ")
number_n1 = (number_n + number_n)
number_n2 = (number_n + number_n + number_n)
a = int(number_n) + int(number_n1) + int(number_n2)
print('Результат n+nn+nnn= ' + str(a))

print("Задача 4")
number = int(input('Введите целое натуральное число: '))
number_r = 0
while number > 0:
    number_d = number % 10
    number //= 10
    if number_d > number_r:
        number_r = number_d
print(number_r)

print("Задача 5")
revenue = float(input('Введите размер выручки: '))
сost = float(input('Введите размер затрат: '))
if revenue > сost:
    profitability = int(revenue - сost) / revenue * 100
    print('Поздравляем! Ваша компания приносить прибыль, а процент рентабельность составляет: ' + str(
        '%.3f' % profitability) + '%')
    staff = int(input('Количество сотрудников составляет: '))
    profitability_staff = float((revenue - сost) / revenue) / staff * 100
    print('Процент рентабельность на одного сотрудника составляет: ' + str('%.3f' % profitability_staff) + '%')
else:
    print('К сожалению ваша компания убыточна')

print("Задача 6")
run = float(input('В первый день пробежал км: '))
plan = float(input('Хочу пробежать км: '))
day_n = 1
while run <= plan:
    print('%.2f' % run)
    run = float(run + (run * 10 / 100))
    day_n = day_n + 1
print('На ' + str(day_n) + ' день спортсмен пробежит не меньше ' + str('%.2f' % plan) + ' километров')
