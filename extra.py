l = int(input('Введите длину массива: '))
arr = [0] * l
for i in range(l):
    print('arr[', i, '] =', end='')
    arr[i] = float(input())
delta = float(input('Введите delta: '))

min = arr[0]
for n in arr:
    if (n > min): min = n

count = 0
for i in range(l):
    if (abs(arr[i] - min) == delta): count += 1
print('В массиве ', count, ' элементов, отличающихся от минимального на delta')