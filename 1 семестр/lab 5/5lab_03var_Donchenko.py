# 3) Дано натуральне число n. Перевірити, чи можна подати n!
# у вигляді добутку трьох послідовних цілих чисел

from math import factorial
a=False
n=int(input('N: '))
for m in range (n):
    for k in range (n):
        if factorial(m)==k*(k+1)*(k+2):
            a=True
            f=factorial(m)
            print('yes, ', k, '*', k+1, '*', k+2, '=', m, '! = ', f)
if a!=True:
    print('no')
    


