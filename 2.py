length = int(input('Введите размер массива:'))
list_a = [0] * length
list_b = [0] * length
from random import randint
for i in range(length) :
    list_a[i] = randint(0, 10)
    list_b[i] = randint(0, 10)

print('Первый массив: ', list_a)
print('Второй массив: ', list_b)

#сортировка позволяет избавится от повторений в выводе
#(наивный алгоритм дает для [1, 2, 2] и [1, 1, 3] вывод [1, 1])
for i in range(1, length-1) :
    for j in range(length - i) :
        if (list_a[j] > list_a[j + 1]): list_a[j], list_a[j + 1] = list_a[j + 1], list_a[j]
        if (list_b[j] > list_b[j + 1]): list_b[j], list_b[j + 1] = list_b[j + 1], list_b[j]

iter1 = 0
iter2 = 0

print('Общие элементы: ')
while iter1 < length and iter2 < length:
    if (list_a[iter1] > list_b[iter2]) : iter2 += 1
    elif (list_a[iter1] < list_b[iter2]) : iter1 += 1
    else:
        print(list_b[iter2])
        iter1 += 1
        iter2 += 1

