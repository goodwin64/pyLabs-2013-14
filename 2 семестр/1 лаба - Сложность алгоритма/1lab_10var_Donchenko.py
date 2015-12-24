# 10. Имеются два упорядоченных по возрастанию списка.
# Требуется получить третий упорядоченный по возрастанию список,
# путем слияния первых двух.

import random

def puzirjok(arr): # использование "пузырька"
    i = len(arr)
    while i > 1:
       for j in range(i - 1):
           if arr[j] > arr[j + 1]:
               arr[j], arr [j+1] = arr [j+1], arr [j]
       i -= 1

def merge (left, right): # слияние по возрастанию
    n, m = 0, 0
    result=[]
    while n < len(left) and m < len(right):
        if left[n] < right[m]:
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

while 1:
    Array1 = []
    Array2 = []
    Array3 = []

    print()
    # Параметры списков
    SizeOfArray1 = input('Кількість елементів першого списку: ')
    if SizeOfArray1=='stop' or SizeOfArray1=='стоп':
        break
    SizeOfArray1=int(SizeOfArray1)
    if SizeOfArray1>=1:
        StartArray1=int(input('Ліва границя першого списку: '))
        EndArray1=int(input('Права границя першого списку: '))
        for k in range(SizeOfArray1):
            z = (random.randint(StartArray1, EndArray1))
            Array1.append(z)
        puzirjok(Array1) # по возрастанию
        print('spisok 1:')
        print(Array1) # вывод массива 1

    print()
    SizeOfArray2 = input('Кількість елементів другого списку: ')
    if SizeOfArray2=='stop' or SizeOfArray2=='стоп':
        break
    SizeOfArray2=int(SizeOfArray2)
    if SizeOfArray2>=1:
        StartArray2=int(input('Ліва границя другого списку: '))
        EndArray2=int(input('Права границя другого списку: '))
        for k in range(SizeOfArray2):
            z = (random.randint(StartArray2, EndArray2))
            Array2.append(z)
        puzirjok(Array2)
        print('spisok 2:')
        print(Array2) # вывод массива 2

    Array3 = merge(Array1, Array2)          

    print()
    print('spisok 3:')
    print(Array3)







    
