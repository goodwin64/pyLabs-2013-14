# 12. Напишите программу, которая вводит с клавиатуры два непустых
# неубывающих списка целых чисел, и печатает те и только те элементы,
# которые встречаются в обоих списках (пересечение множеств).

# то есть убираем дубли в обоих списках, конкатенируем их и выводим дубли
# из получившегося списка

import random

def puzirjok(arr): # использование "пузырька"
    i = len(arr)
    while i > 1:
       for j in range(i - 1):
           if arr[j] > arr[j + 1]:
               arr[j], arr [j+1] = arr [j+1], arr [j]
       i -= 1

def merge (left, right): # 2 массива конкатенируются в 3-й массив
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

Array1 = []
Array2 = []
Array3 = []
Crossing_of_arrays=[]

print()
# Параметры списков
SizeOfArray1 = int(input('Кількість елементів першого списку: '))
for k in range(SizeOfArray1):
    z = int(input('element: '))
    Array1.append(z)
puzirjok(Array1) # по возрастанию
print('spisok 1:')
print(Array1) # вывод массива 1
x=0
while x<len(Array1)-1:
    if Array1[x]==Array1[x+1]:
        del Array1[x]
        x-=1
    x+=1

print()
# Параметры списков
SizeOfArray2 = int(input('Кількість елементів другого списку: '))
for k in range(SizeOfArray2):
    z = int(input('element: '))
    Array2.append(z)
puzirjok(Array2) # по возрастанию
print('spisok 2:')
print(Array2) # вывод массива 2
x=0
while x<len(Array2)-1:
    if Array2[x]==Array2[x+1]:
        del Array1[x]
        x-=1
    x+=1

Array3 = merge(Array1, Array2)

x=0
while x<len(Array3)-1:
    if Array3[x]==Array3[x+1]:
        Crossing_of_arrays.append(Array3[x])
    x+=1

    
print()
print('Пересечение множеств:')
print(Crossing_of_arrays)







    
