# 8. Дан список заполненный случайным образом,
# где некоторые числа могут повторяться. Получите отсортированный
# список, в которым не будет содержаться чисел, который повторялись.

import random
import sys

def swap(array, i, j): # функция, которая меняет 2 элемента местами
    array[i], array[j] = array[j], array[i]
 
def SelectionSort(mylist): #Сортировка выбором
    ln=len(mylist) 
    for k in range(ln-1):#-1, т.к. последний элемент обменивать уже не надо
        m = k #в m хранится минимальное значение
        i = k + 1#откуда начинать поиск минимума (элемент следующий за k)
        while i < ln:
            if mylist[i] < mylist[m]:
                m = i
            i += 1
        if k!=m:
          swap(mylist, k, m)
    return mylist

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
        z=(random.randint(1, 5)) # работа random'a только с целыми числами
        Array.append(z)
    print('Без сортировки: ')
    print()
    print(Array)
    SelectionSort(Array)
    print()
    print('С сортировкой: ')
    print()
    print(Array)
    print()

    x=0 # искуственный for ... in
    while x<len(Array)-1:
        if Array[x]<Array[x+1]: # в случае, если элемент меньше следующего, 
            x+=1 # идем дальше
        else: # иначе (равен, поскольку список отсортирован) - 
            del Array[x] # удаляем этот элемент, следующий становится на его позицию

    print ('Без дублей --->', tuple(Array))
    print()
            










    
