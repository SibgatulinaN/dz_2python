# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.


n=int(input("введите число N: "))
p=0
while 2 ** p <=n:
        print(2**p,end=' ')
        p +=1
   
