# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

N = abs(int(input('Введите число N ')))
stop = 0
K = 2
for i in range(N):
    if stop != 1:
        K = K ** i
        if K <= N:
            print(K, end=' ')
            K = 2
        else:
            stop = 1
    else:
        i = N