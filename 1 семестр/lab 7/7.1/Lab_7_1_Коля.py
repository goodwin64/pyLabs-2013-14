# -*- coding: cp1251 -*-
E=0.001
m=''
x=(raw_input("Введіть x: "))
z=(raw_input("Введіть z: "))
while x=="":
     x=(raw_input("Введіть x: "))
while z=="":
     z=(raw_input("Введіть z: "))
x=float(x)
z=float(z)
def step(ch, st=1):
    n=2
    ch1=ch
    while n<=st:
        ch1=ch1*ch
        n=n+1
    return ch1
if (z-(step(x,9)/3))==0:
    print ("--------------------")
    print ('error')
else:
    m=(x*x)/(z-(step(x,9)/3))
    def mod(m):
       if m>0:
           return m
       elif m==0:
           return 0
       else:
           return -m
    m=mod(m)
    if (step(z,2)-m)==0:
        print ("--------------------")
        print ('erorr')
    else:
        y=z+(x/(step(z,2) - m))
        print ("--------------------")
        print ('y:'), y
