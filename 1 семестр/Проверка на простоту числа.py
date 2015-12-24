from math import sqrt
n_str=input('Введите число для проверки: ')
n=float(n_str)
def prime(n, k=2):
    if n<0: # для отрицательных чисел
        return False
    while k<sqrt(n):
        if n%k==0:
            return False
        k+=1
    if n%k!=0 and n-int(n)==0 and n>=3 or n==2:
        return True

print('простое ли число', n_str, '?')
if prime(n)==True:
        print('Да, число', n_str, 'простое')
if prime(n)!=True:
        print('Нет, число', n_str, 'не простое')
        
