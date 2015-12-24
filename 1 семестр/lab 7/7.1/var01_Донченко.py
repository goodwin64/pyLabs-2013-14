# Don FE-3106

epsilon = 1e-4
import math

#Функция№1

def faktorial(x):                   
    if x>=1:
        c=x*faktorial(x-1)
    elif x==0:
        c=1
    elif x<0 or type(x)!=int:
            valErr=Exception("Аргумент функции faktorial должен быть целым неотрицательным числом")
            raise valErr
    return c

def myAbs(n):
    if (n < 0):
        return -n
    return n

def myPow(x, n):
    result = 1.0
    for i in range (0, n):
        result *= x
    return result

def myPowDivideByFactorial(x, m):
    #formula is myPow(x, m) / fact(m)
    if (m == 0):
        return 1.0
    return float(x)/m * myPowDivideByFactorial(x, m - 1)

def shTailor(x, n):
    m = 2 * n + 1
    #result = myPow(-1.0, n) * myPow(x, m) / fact(m)
    result = myPowDivideByFactorial(x, m)
    return result

def chTailor(x, n):
    m = 2 * n
    #result = myPow(-1.0, n) * myPow(x, m) / fact(m)
    result = myPowDivideByFactorial(x, m)
    return result

def sinTailor(x, n):
    x = x % (2 * 3.14159265359)
    if (n % 2 == 0):
        return shTailor(x,n)
    return -shTailor(x,n)

def cosTailor(x, n):
    x = x % (2 * 3.14159265359)
    if n % 2 == 0:
        return chTailor(x,n)
    return -chTailor(x,n)

def calcSumOfTailor(x, TailorFunc):
    result = 0
    n = 0    
    while (True):
        xn = TailorFunc(x, n)
        if (myAbs(xn) < epsilon):
            return result
        result += xn
        n += 1
        
def mySin(x):    
    return calcSumOfTailor(x, sinTailor)

def myCos(x):    
    return calcSumOfTailor(x, cosTailor)




#Вычисления
a=int(input("Введите a:"))
b=int(input("Введите b:"))
if 2*a+b!=0 and myCos(b)!=0: 
    y=(a-faktorial(6))/(2*a+b)+mySin(3*a)/myCos(b)
    print(y)
else:
    print ('ODZ')
