# 1. Дан список заполненный строками, в котором
# некоторые строки могут повторяться. Получите
# отсортированный список со строками без повторений.        

import random

def swap(arr, i, j): # функция, которая меняет 2 элемента местами
    arr[i], arr[j] = arr[j], arr[i]
 
def Sortiruem(arr): # использование "пузырька", при этом сравнивать можно и строки
    i = len(arr)
    while i > 1:
       for j in range(i - 1):
           if arr[j] > arr[j + 1]:
               swap(arr, j, j + 1)
       i -= 1

def delete_dubles(Array): # проверка "равны ли соседние элементы"
    for E in range (len(Array)-1):
        if Array[E] == Array[E+1]:
            del Array[E]
            E -= 1
    return Array    

# Размер дальнейшего списка
SizeOfArray=int(input('Введіть розмір подальшого списку - кількість елементів у ньому: '))

# наш список
Array=[]

# аппенд - добавляет к списку на последнюю позицию элемент
for k in range(1, SizeOfArray+1):
    z=input('your fraze: ') # работа random'a только с целыми числами
    Array.append(z)
    
print('Было', len(Array), 'элементов')
print()
print('Неотсортированный список: ', Array)
Sortiruem(Array)
print('Отсортированный список: ', Array)
print()

delete_dubles(Array)
    
print ('--->', tuple(Array))
print('Стало', len(Array), 'элементов')
            










    
