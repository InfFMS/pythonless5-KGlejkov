# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]
N=int(input())
M=[]
from random import randint
mas=[randint(10,100000) for i in range(N)]
print(mas)
def f(mas):
    for i in mas:
        if i>10 and i<100 and i%10==i//10:
            M.append(i)
        elif i>100 and i<1000 and i%10==(i//10)%10==i//100:
            M.append(i)
        elif i>1000 and i<10000 and i%10==(i//10)%10==(i//100)%10==i//1000:
            M.append(i)
        elif i>10000 and i<100000 and i%10==(i//10)%10==(i//100)%10==(i//1000)%10==i//10000:
            M.append(i)
print(f(mas))

        
        

