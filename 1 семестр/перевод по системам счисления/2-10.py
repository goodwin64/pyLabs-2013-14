x=input('x:') # для чисел, записанных только цифрами 0 и 1
a=0 # сумма всех произведений

i=len(x)-1
while i>0:
    for k in range(len(x)):
        m=int(x[k])
        n=m*(2**i)
        a+=n
        i-=1

print(a)
