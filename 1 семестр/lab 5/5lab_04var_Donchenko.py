# 4) Написати програму виведення всіх чисел
# від 1 до N, які закінчуються цифрою 3.

N=input('Введіть число N: ')
for i in range (1, int(N)+1):
    if str(i)[-1]=='3':
        print (i)
