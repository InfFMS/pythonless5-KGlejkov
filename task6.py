# Массив имеет четное число элементов N.
# Заполнить массив случайными числами и
# выполнить реверс отдельно в первой половине и второй половине.
# Пример: ввод N = 6
# [1,2,3,4,5,6]
# Вывод: [3,2,1,6,5,4]
N=int(input())
M=[] 
D=[] 
F=[]
from random import randint
mas=[randint(0,1000) for i in range(N)]
print(mas)
for j in range(len(mas)//2):
    M.append(mas[j])
m=mas
M.reverse()
mas.reverse() 
for k in range(len(mas)//2):
    D.append(mas[k]) 
for i in range(len(M)):
    F.append(M[i])
for j in range(len(D)):
    F.append(D[j])
print(F)
