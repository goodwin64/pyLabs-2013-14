a=[]
x=int(input('x: '))
m=0
while x!=0:
    m=x%16
    x=int(x/16)
    if m<=9:
        a.append(int(m))
    elif m==10:
        a.append('a')
    elif m==11:
        a.append('b')
    elif m==12:
        a.append('c')
    elif m==13:
        a.append('d')
    elif m==14:
        a.append('e')
    elif m==15:
        a.append('f')
a.reverse()
print(a)
