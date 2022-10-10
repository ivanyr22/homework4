length = int(input('Введите размер массива:'))
list_ = [0] * length
from random import randint
for i in range(length) :
    list_[i] = randint(0, 100)
print('Исходный массив: ', list_)
max = list_[0]
max_index = 0
for i in range(length):
    if (list_[i] > max):
        max = list_[i]
        max_index = i
for j in range(max_index + 1, length):
    list_[j] = 0
print('Измененный массив: ', list_)