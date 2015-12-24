# 15) Вивести всі прості числа до числа n, різниця
# між якими дорівнює 6, тобто (p, p + 6).
# Наприклад (5,11), (7,13), (11,17), (13,19), (17,23), …

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

n=int(input('n: '))
for k in range (n):
    if prime(k+6)==True and prime(k)==True:
        print(k, k+6)
