# Задача №9.
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

number = int(input('Введите число: '))
i = 1
f = 1
if number == 0:
    f = '0! = 1'
elif number < 0:
    f = 'Введенное число не соответствует требованиям'
else:
    while i < number + 1:
        f *= i
        i += 1
print(f)
#2 решение
n = int(input('Введите число: '))
factorial_ = 1
for i in range(1, n + 1):
    factorial_ *= i
print(factorial_)
 #3

from math import factorial
n = int(input('Введите число: '))
print(factorial(n))