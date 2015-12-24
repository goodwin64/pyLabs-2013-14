from math import sqrt
n=float(input('n='))
k=3
c=3
E=0.0001
b=0
if n<=2:
    print('nema')
while k<int(n):
    z=k/2
    if (z-int(z))<E:
        b=1
    while c<k:
        z=k/c
        if (z-int(z))<E:
            b=1
        c+=2
    if b==0:
        print(k)
    b=0
    k+=2
    c=3
