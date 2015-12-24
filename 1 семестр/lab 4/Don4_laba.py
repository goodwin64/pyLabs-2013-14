# Lab4, Donchenko Max, FE-3106
print('STZI, Lab4')
print('Donchenko Max, FE-3106')
N=int(input('Введите N: '))
M=int(input('Введите M: '))
a=0
i=0
if (M-N<0):
    N=M+N
    M=N-M
    N=N-M
a=M-N+1   
for i in range(a):
    i=i+N
    if i%2==0 and i%3==0:
        print(i)
    elif i%2==0 or i%3==0:    
        if i%2==0:
            print(i)
        if i%3==0:
            print(i)
    elif i%2!=0 and i%3!=0:
        print('Нет таких чисел')
    
    
    
    

      
      
