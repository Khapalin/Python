# Найти факториал числа n
# 3 = 6
# 5 = 120

n = int(input())
i = 1
result = 1
while i <= n:
    result *= i
    i += 1
print(result)