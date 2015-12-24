# 6. Дан список заполненный случайным образом, где
# некоторые числа могут повторяться. Получите отсортированный
# список с числами без повторений.

from random import randint

def swap(arr, i, j): # функция, которая меняет 2 элемента местами
    arr[i], arr[j] = arr[j], arr[i]
 
def Bubble(arr): # использование "пузырька"
    i = len(arr)
    while i > 1:
       for j in range(i - 1):
           if arr[j] > arr[j + 1]:
               swap(arr, j, j + 1)
       i -= 1

while True:
    # Размер дальнейшего списка
    SizeOfArray=input('Введіть розмір подальшого списку - кількість елементів у ньому: ')
    if SizeOfArray=='stop' or SizeOfArray=='стоп':
        break
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
        print()
        continue

    # аппенд - добавляет к списку на последнюю позицию элемент
    for k in range(1, SizeOfArray+1):
        z=randint(1, 5) # работа random'a только с целыми числами
        Array.append(z)
    print('Без сортировки: ')
    print(Array)
    Bubble(Array)
    print()
    print('С сортировкой: ')
    print(Array)
    print()

    x=0 # искуственный for ... in
    while x<len(Array)-1:
        if Array[x]<Array[x+1]: # в случае, если элемент меньше следующего, 
            x+=1 # идем дальше
        else: # иначе (равен, поскольку список отсортирован) - 
            del Array[x] # удаляем этот элемент, следующий становится на его позицию

    print ('--->', tuple(Array))
    print()
            










    
