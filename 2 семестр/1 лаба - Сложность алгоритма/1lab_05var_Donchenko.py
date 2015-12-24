# 5. Дан одномерный вещественный список из N элементов,
# заданных случайными числами на промежутке [a; b). Выполните
# циклический сдвиг элементов с n -ой позиции вправо на k позиций.

import random

def displacement(Array, k):
        if k>len(Array) - 1:
            while k>len(Array) - 1:
                k-=len(Array)
        elif k<0:
            while k<0:
                k+=len(Array)
        return Array[-k:]+Array[:-k]

while True:
    # Размер дальнейшего списка, он же len(Array)
    SizeOfArray=int(input('Введіть розмір подальшого списку - кількість елементів у ньому: '))

    # наш список
    Array=[]

    a=int(input('Введите левую границу: '))
    b=int(input('Введите правую границу: '))
    k=int(input('На сколько сдвигаем?   '))
    
    # аппенд - добавляет к списку на последнюю позицию элемент
    for E in range(1, SizeOfArray+1):
        z=(random.randint(a, b)) # работа random'a только с целыми числами
        Array.append(z)
    print(Array)
    print()
    print(displacement(Array, k))
    
    










    
