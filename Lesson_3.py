print('Задача №1')


def my_func(a, b):
    try:
        a, b = int(a), int(b)
        my_num = a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
    except ValueError:
        return "Ошибка"
    return round(my_num, 3)


print(my_func(input('Введите значение №1: '), input('Введите значение №2: ')))

print('Задача №2')


def my_data(**kwargs):
    return " ".join(kwargs.values())


print(my_data(name=input('Введите имя: '), surname=input('Введите фамилию: '), birthday=input('Ваша дата рождения: '),
              city=input('Введите место жительства: '), email=input('Введите email: '),
              num=input('Введите номер телефона: ')))

print('Задача №3')


def my_func1(a, b, c):
    return sum(sorted([a, b, c])[1:])


a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
print(my_func1(a, b, c))

print('Задача №4')


def my_func2(a, b):
    try:
        c = a ** b
    except TypeError:
        return "Ошибка"
    return c


a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
print(my_func2(a, b))

print('Задача №5')


def my_func3():
    a = 0
    while True:
        my_list = input("Введите число или введите q для выхода: ").split()
        for num in my_list:
            if num == 'q':
                return a
            else:
                try:
                    a += int(num)
                except ValueError:
                    print("Для выхода из программы нажмите 'q': ")
        print(f"Сумма чисел = {a}")


print(my_func3())

print('Задача №6')


def int_func4():
    for word in input("Введите слова через пробел (строчная латиница):").split():
        chars = 0
        for chars in word:
            if 97 <= ord(chars) <= 122:
                chars = chars + 1
        print(word.title() if chars == len(word) else f"{word} - Прописные буквы!!!")


int_func4()
