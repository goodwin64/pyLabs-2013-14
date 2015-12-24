x=input('x:') # для чисел, записанных только цифрами
a=0 # сумма всех произведений

i=len(x)-1
while i>0:
    for k in range(len(x)):
        m=int(x[k])
        n=m*(16**i)
        a+=n
        i-=1

print(a)
