# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.
# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.
from random import randint
N=int(input())
mas=[randint(0, 1000)for i in range(N)]
print(max(mas))
a=0
for i in range(N):
    if max(mas)==mas[i]:
        a+=1
print(a)
