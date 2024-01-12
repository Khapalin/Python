#Дан массив, состоящий из целых чисел. Напишите
#программу, которая в данном массиве определит
#количество элементов, у которых два соседних и, при
#этом, оба соседних элемента меньше данного. Сначала
#вводится число N — количество элементов в массиве
#Далее записаны N чисел — элементы массива. Массив
#состоит из целых чисел.


import random

len1 = int(input("Размер список: "))
lst1 = [random.randint(0, 10) for _ in range(len1)]
print(lst1)
count = 0
for i in range(1, len1 - 1):
    if lst1[i] > lst1[i - 1] and lst1[i] > lst1[i + 1]:
        count += 1


# list comprehension
result = [1 for i in range(1, len1 - 1) if lst1[i] > lst1[i - 1] and lst1[i] > lst1[i + 1]]

print(count)
print(result.count(1))