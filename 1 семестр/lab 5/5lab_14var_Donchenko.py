# 14) Вивести 5 простих чисел, які більші введеного числа.

from math import sqrt

def prime(x):
    if x<2:
        return False
    elif x-int(x)!=0:
        return False
    for k in range (2, int(sqrt(x)+1)):
        if x%k==0:
            return False
    else:
        return True

n=int(float(input('n: '))+1)
counter=0
while counter<5:
    if prime(n)==True:
        counter+=1
        print(n)
    n+=1
