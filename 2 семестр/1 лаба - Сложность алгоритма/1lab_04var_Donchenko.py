# 4. Имеются два упорядоченных по убыванию списка.
# Требуется получить третий упорядоченный по убыванию список,
# путем слияния первых двух.

import random

def insertion_sort(A):
    for i in range (1, len(A)):
        buffer = A [i]
        j = i - 1
        while j >= 0 and A[j] < buffer:
            A [j + 1] = A [j]
            j -= 1
        A [j+1] = buffer
    return A

def merge (left, right): # слияние по убыванию
    n, m = 0, 0
    result=[]
    while n < len(left) and m < len(right):
        if left[n] > right[m]:
            result.append(left[n])
            n += 1
        else:
            result.append(right[m])
            m += 1
    while n < len(left):
        result.append(left[n])
        n+=1
    while m < len(right):
        result.append(right[m])
        m+=1
    return result

# Параметры списков
SizeOfArray1 = int(input('Кількість елементів першого списку: '))
StartArray1=int(input('Ліва границя першого списку: '))
EndArray1=int(input('Права границя першого списку: '))
print()
SizeOfArray2 = int(input('Введіть розмір другого списку: '))
StartArray2=int(input('Ліва границя другого списку: '))
EndArray2=int(input('Права границя другого списку: '))
print()

Array1 = []
Array2 = []
Array3 = []

for k in range(1, SizeOfArray1 + 1):
    z = (random.randint(StartArray1, EndArray1))
    Array1.append(z)
insertion_sort(Array1)
print(Array1) # вывод массива 1
print('+')

for k in range(1, SizeOfArray2 + 1):
    z = (random.randint(StartArray2, EndArray2))
    Array2.append(z)
insertion_sort(Array2)
print(Array2) # вывод массива 2
print('=')    

Array3 = merge(Array1, Array2)

print(Array3)







    
