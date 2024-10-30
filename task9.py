# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]
N=int(input())
from random import randint
mas=[randint(0,10) for i in range(N)]
print(mas)
markiz=[mas[0]]
for i in mas:
    for j in markiz:
        if i!=j:
            markiz.append(i)
print(markiz)
