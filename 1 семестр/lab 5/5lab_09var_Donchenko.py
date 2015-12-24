# 9) Знайти максимальне значення функції
# y=sin(x*х)*x+cos(x), на відрізку [c,d] з кроком 0.001

from math import sin, cos

shag=0.001
c=float(input('c: '))
c1=float(c)
d=float(input('d: '))
max=sin(c**2)*c+cos(c)
while c<=d:
    if max<sin(c**2)*c+cos(c):
        max=sin(c**2)*c+cos(c)
    c+=shag

print ('max(y) from', c1, 'to', d, '=', max)
