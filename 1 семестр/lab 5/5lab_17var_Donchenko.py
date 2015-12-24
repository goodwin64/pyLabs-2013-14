# 17) Написати програму, яка виводить
# всі числа Мерсена від 1 до n.

from math import log, sqrt

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

while True:
    n_max_str=input('n: ')
    if n_max_str=='STOP':
        break
    n_max=int(n_max_str)
    p_max=int(log(n_max+1, 2)) # 2^p-1=n отсюда p=log(n+1, осн2)
    print(p_max)
    lsMersena=[] # итоговый список
    Array_of_prime=[] # все простые числа вплоть до p_max
    for k in range (p_max):
        if prime(k)==True:
            Array_of_prime.append(k)
    for p in Array_of_prime:
        n=2**p-1
        if prime(n)==True:
            lsMersena.append(n)
    print(lsMersena)
