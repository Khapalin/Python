"""
Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y ≤ 1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3
"""

summa = int(input('Введите сумму чисел: '))
proiz = int(input('Введите произведение чисел: '))
a = 0
for x in range(summa):
    for y in range(summa):
        if x + y == summa and x * y == proiz:
            a += 1
            print(f"Первое число {x}, второе число {y}")

"""
for x in range(s):
    y = s - x
    if x + y == s and x * y == p:
        
        print(x, y)
        break
"""
"""
summa = int(input('Введите сумму чисел: '))
product = int(input('Введите произведение чисел: '))
for x in range(summa):
    for y in range(x, summa):
        if x + y == summa and x * y == product:
            print(x, y)
"""
            