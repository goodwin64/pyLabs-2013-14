# 11. Напишите программу, которая вводит с клавиатуры два непустых
# неубывающих списка целых чисел, и печатает те и только те элементы,
# которые встречаются хотя бы в одном из списков (объединение множеств).

# то есть сначала конкатенируем массивы 1 и 2, а потом убираем дубли
# из получившегося массива 3 - получаем уникальные элементы, которые есть
# хотя бы в одном из 2-х массивов

import random

def puzirjok(arr): # сортировка "пузырьком"
    i = len(arr)
    while i > 1:
       for j in range(i - 1):
           if arr[j] > arr[j + 1]:
               arr[j], arr [j+1] = arr [j+1], arr [j]
       i -= 1
       
def merge (left, right): # 2 половины массива
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
    
def mergesort(Array): # сортировка слиянием
    if len(Array) < 2:
        return Array[:]
    mid = int(len(Array)/2)
    left = mergesort(Array[:mid])
    right = mergesort(Array[mid:])
    merge (left, right)
    return merge (left, right)

def delete_dubles(Array):
    E = 0
    while E < len(Array)-1:
        if Array[E] == Array[E+1]:
            del Array[E]
            E -= 1
        E += 1
    return Array

# Переменные

Array1 = []
Array2 = []
Fusion_of_arrays = [] # Fusion - объединение

print()

# Параметры списков
SizeOfArray1 = int(input('Кількість елементів першого списку: '))
for k in range(SizeOfArray1):
    z = int(input('element: '))
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# если надоест вводить вручную элементы - перед z сверху поставишь решетку
# а снизу уберешь и в скобках после рандинт введешь границы, сейчас от 1 до 100
#    z = random.randint(1, 100)
    Array1.append(z)
puzirjok(Array1) # по возрастанию
print('spisok 1:')
print(Array1) # вывод массива 1

print()
# Параметры списков
SizeOfArray2 = int(input('Кількість елементів другого списку: '))
for k in range(SizeOfArray2):
    z = int(input('element: '))
    Array2.append(z)
puzirjok(Array2) # по возрастанию
print('spisok 2:')
print(Array2) # вывод массива 2
Fusion_of_arrays = mergesort(Array1[:] + Array2[:]) # при слиянии 1-го и 2-го получаем 3-й
Fusion_of_arrays = delete_dubles(Fusion_of_arrays) # удаляем повторяющиеся элементы

print()
print('Объединение множеств:')
print(Fusion_of_arrays)







    
