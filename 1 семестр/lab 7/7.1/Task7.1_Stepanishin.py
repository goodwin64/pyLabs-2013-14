#Функция№1

def stepen(x,n):                     
    if type(n)!=int:
        valErr=Exception("Показатель степени в stepen должен быть целым числом")
        raise valErr
    if n>0:
        c=x*stepen(x,n-1)
        return c
    if n<0:
        c=1/x*stepen(x,n+1)
        return c
    if n==0:
        return 1
    return c

#Функция№2

def faktorial(x):                   
    if x>=1:
        c=x*faktorial(x-1)
    elif x==0:
        c=1
    elif x<0 or type(x)!=int:
            valErr=Exception("Аргумент функции faktorial должен быть целым неотрицательным числом")
            raise valErr
    return c

#Вычисления
x=0
z=0
while z==stepen(x,2)/4:
    x=int(input("Введите х:"))
    z=int(input("Введите z:"))
y=x-z/(z-stepen(x,2)/4)-stepen(x,2)/faktorial(9)
print(y)
