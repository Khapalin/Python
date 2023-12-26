"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

10 -> 1 2 4 8
"""


number = int(input('Введите число: '))
stepen = 0
result = 1
while result < number + 1:
    print(result, end=' ')
    stepen += 1
    result = 2 ** stepen
