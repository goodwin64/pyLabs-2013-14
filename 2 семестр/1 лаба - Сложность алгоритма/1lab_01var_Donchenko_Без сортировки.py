# 1. Дан список заполненный строками, в котором
# некоторые строки могут повторяться. Получите
# отсортированный список со строками без повторений.

import random
import sys

while True:
    # Размер дальнейшего списка
    SizeOfArray=input('Введіть розмір подальшого списку - кількість елементів у ньому: ')

    # На случай, если не введено ничего
    while SizeOfArray=='':
        SizeOfArray=input('Введіть розмір подальшого списку - кількість елементів у ньому: ')
    SizeOfArray=int(SizeOfArray)
    # На случай, если введено целое, но отрицательное
    while SizeOfArray<0:
        SizeOfArray=input('Введіть розмір подальшого списку - кількість елементів у ньому: ')
        while SizeOfArray=='':
            SizeOfArray=input('Введіть розмір подальшого списку - кількість елементів у ньому: ')

    # наш список
    Array=[]

    # если длина списка 0 (пустой), то...
    if SizeOfArray==0:
        print('список порожній')
        sys.exit()

    # аппенд - добавляет к списку на последнюю позицию элемент
    for k in range(1, SizeOfArray+1):
        z=str(random.randint(1, 5)) # работа random'a только с целыми числами
        Array.append(z)
    print(Array)

    x=0
    while True:
        if x>=len(Array): # ограничение на индекс, чтоб был меньше длины массива
            break
        E=Array[x] # 
        if Array.count(E)==1: # в случае, если элемент не повторяется, переходим к следующему
            x+=1
        else:
            while Array.count(E)>1: # и в случае повторений элементов 
                del Array[Array.index(E)] # удаляем из него те элементы, которые повторяются

    print ('--->', tuple(Array))
    print()
            










    
