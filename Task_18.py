# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.


import random

num = int(input("Введите число, длину массива -> "))
list = []
for i in range(num):
    list.append(random.randint(1, num))

print(list)

findNum = int(input("Введите число, которое хотите проверить -> "))
up = findNum
down = findNum

for i in list:
    down = int(down - 1)
    up = int(up + 1)
    for i in list:
        if i == down:
            print(f"Ближайщее число к {findNum} - {i}")
            exit(1)
        if i == up:
            print(f"Ближайщее число к {findNum} - {i}")
            exit(1)