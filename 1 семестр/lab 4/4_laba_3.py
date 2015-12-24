# lab_4_3 Донченко Максим
# Нахождение корня из числа

from math import *
a=float(input('a=')) # число, из которого берется корень
E=0.0001 # точность е-4

while (a<0):
    print('Число А менше за 0')
    a=float(input('a='))
    
x1=float(input('x1='))

while (x1<E):
    print ('Ділення на 0 неможливе')
    print ('Введіть будь-яке число, більше за', E, ': ')
    x1=float(input('x1='))
x2=(1/2)*(x1+(a/x1)) # ответ (х2 - корень из а)

while (abs(x1-x2)>=E):
    x1=x2
    x2=(1/2)*(x1+(a/x1))
print(round(float(x2), 4))
