n=int(input('Размер='))
i=1
a=[]
b=[]
d=0
p=0
r=int(n-1/2)
E=0.0001
while i<=n:
    a.append(int(input('element=')))
    i+=1
a.sort()
a.reverse()
x=int(input('x='))
if n==0:
    c=(x, -1)
    print(c)
elif a[0]<x:
    c=(x, -2)
    print(c)
elif a[n-1]>x:
    c=(x, -3)
    print(c)
else:
    while d<n-1:
        if x>=a[r]:
            n=r
        else:
            d=r
        r=int((n+d)/2)
        if a[n]==x:
            b=(int(x), n)
            print(b)
            break
        if r==0:
            break

print (tuple(b))
