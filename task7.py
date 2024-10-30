# Заполнить массив длины N случайными числами в интервале [-100,100] и
# переставить элементы так, чтобы все положительные элементы
# стояли в начала массива, а все отрицательные и нули в конце.
# Пример: ввод N = 6
# [20, -90, 15, -34, 10, 0]
# Вывод: [20, 15, 10, -90, -34, 0]
N=int(input())
from random import randint
mas=[randint(-1,1) for i in range(N)]
MAS=[]
for i in mas:
    if i>0:
        MAS.append(i)

for k in mas:
    if k<0:
        MAS.append(k)
        
for j in mas:
    if j==0:
        MAS.append(j)

print(MAS)


        
    
