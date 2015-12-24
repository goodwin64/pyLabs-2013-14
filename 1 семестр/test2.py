n=int(input('Размер='))
i=1
a=[]
while i<=n:
    i+=1
    a.append(int(input('введіть елемент: ')))
a.sort()
a.reverse()
print(a)
a.reverse()
x=int(input('x='))

start = 1 
end = len(a) 
center = int((start + end) / 2) 
while a[center] != x or start > end: 
    
    center = int((start + end) / 2) 
    if x > a[center]: start = center + 1 
    else: end = center - 1 
if start > end:
     print ("Элемент не найден")
else:
     print (center)
