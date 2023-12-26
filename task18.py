"""
i = 0
min_num = abs(list_1[0] - k)
index = 0
while i < len(list_1):
    if abs(list_1[i] - k) < min_num:
        min_num = abs(list_1[i] - k)
        index = i
    i += 1
print(list_1[index])

"""

n = int(input('Введите количество элементов в массиве: '))

list = []

for i in range(n):
    list.append(int(input('Введите элемент массива: ')))
print(list)

x = int(input('Введите число: '))

k = 0 #сюда положим индекс элемента массива, с которым у Х наименьшая разница
minDiff = abs(x - list[0]) #сюда положим минимальную разницу между числом Х и элементом массива, предположим, что мин разница с первым элементом

for i in range(n):
    if abs(x - list[i]) <= minDiff:
        minDiff = abs(x - list[i])
        k = i
print(list[k])