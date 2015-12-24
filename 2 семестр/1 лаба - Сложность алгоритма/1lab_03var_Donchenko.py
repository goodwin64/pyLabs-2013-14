# 3. Список размером m, где m – натуральное число, заполнен
# случайным образом. Найдите в списке моду. Модой называется
# элемент ряда, который встречается наиболее часто.

import random

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

    # аппенд - добавляет к списку на последнюю позицию элемент
    for k in range(1, SizeOfArray+1):
        z=(random.randint(1, 2)) # работа random'a только с целыми числами
        Array.append(z)
    
    moda=Array[0]
    count_of_moda=Array.count(moda)
    for k in Array:
        if count_of_moda<Array.count(k):
            count_of_moda=Array.count(k)
            moda=k
            
    print(Array, '-----> moda', moda, ', tak kak vstrechaetsya', count_of_moda, 'raz')
            










    
