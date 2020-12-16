print('Задача №1')
my_list = [55, 23.32, 'Привет', (43, 76, 76.89), {1, 2, 3, 4, 5}, {22: 'Hi', 8: 'Ok'}, True, False]
for num, el in enumerate(my_list, 1):
    print(f"{num}) {el} - {type(el)}")

print('Задача №2')
my_list = list(input('Введите значения: '))
for el in range(1, len(my_list), 2):
    my_list[el - 1], my_list[el] = my_list[el], my_list[el - 1]
print(my_list)

print('Задача №3')
seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}

month = int(input('Введите месяц: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)

print('Задача №4')
n = input('Введите строку из нескольких слов: ').split()
for el, word in enumerate(n, 1):
    print(f"{el} {word[:10]}")

print('Задача №5')
rating = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number = int(input('Введите значение: '))
n = 0
for i in rating:
    if number <= i:
        n += 1
rating.insert(n, number)
print(rating)

print('Задача №6')
# Набрал готовый код, чтобы прошагать
goods = []
features = {'название': '', 'цена': '', 'количество': '', 'еденица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'еденица измерения': []}
num = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжениия "Enter": ').upper() == 'Q':
        break
    num +=1
    for f in features.keys():
        pro = input(f'Введите значение свойства "{f}": ')
        features[f] = int(pro) if f == 'цена' or f == 'количество' else pro
        analytics[f].append(features[f])
    goods.append((num, features))
    print(f"\nСтруктура товаров\n{goods}")
    print(f'\n Текущая аналитика по товарам: \n {"*" * 30}')
    for key, value in analytics.items():
        print(f'{key[:25]:>30}: {value}')

    print("*" *30)
