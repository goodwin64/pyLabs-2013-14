# 1 СПОСОБ

a=[]
x=int(input('x: '))
m=0
while x!=0:
    m=x%2
    x=int(x/2)
    a+=str(m)
a.reverse()
print(a)

# 2 СПОСОБ

x = int(input("Введите натуральное число: "))
n = ""
 
while x > 0:
    y = str(x % 2)
    n = y + n
    x = int(x / 2)
 
print (n)
