"""# Задача №1
with open('one.txt', 'w', encoding='utf-8') as a:
    while True:
        line = input("Введите новую строку или пустую строку для завершения: ")
        if not line:
            break
        print(line, file=a)"""

"""my_name = input('Файл: ')
a = open(my_namename,'w')
while True:
    s = input()
    if s == '': break
    a.write(s+'\n')
a.close()"""

# Задача №2 (Работает с файлом созданным в задаче 1)
a = open('one.txt')
line = 0
for i in a:
    line += 1

    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(i, len(i), 'симв.', word, 'сл.')

print(line, 'стр.')
a.close()
# Задача №3
with open("text_3.txt", "r", encoding="utf-8") as f:
    my_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    # print(my_dict)
    print(f'Средняя зарплата руб.: {round(sum(my_dict.values()) / len(my_dict), 2)} \n'
          f'Работники с заработной платой больше 20 000 руб.: {[el[0] for el in my_dict.items() if el[1] < 20000]}')

# Задача №4

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text_4.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('file_4_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

# Задача №5

from random import randint

with open('text_8', 'w', encoding='utf-8') as f:
    my_list = [randint(1, 50) for k in range(50)]
    f.write(" ".join(map(str, my_list)))
    print(f'Сумма чисел = {sum(my_list)}')

# Задача №6

my_dict = {}
with open("text_6.txt", encoding='utf-8') as f:
    for line in f:
        name, stats = line.split(':')
        name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        my_dict[name] = name_sum
print(f"{my_dict}")

# Задача №7

import json

with open('my_j.json', 'w', encoding='utf-8') as a:
    with open('text_7.txt', encoding='utf-8') as b:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in b}
        result = [profit, {"average_profit": round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                   len([int(i) for i in profit.values() if int(i) > 0]))}]
json.dump(result, a, ensure_ascii=False, indent=4)
