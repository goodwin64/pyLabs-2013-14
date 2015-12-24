# 4) Знайти мінімальне та максимальне значення у списку
# довільної довжини та обміняти їх місцями. У результаті має
# бути кортеж, який містить список з обміняними місцями
# максимальним та мінімальним елементами

import random
import sys

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
List=[]

# если длина списка 0 (пустой), то...
if SizeOfArray==0:
    print('список порожній')
    sys.exit()

# аппенд - добавляет к списку на последнюю позицию элемент
for k in range(1, SizeOfArray+1):
    z=(random.randint(0, 10)) # работа random'a только с целыми числами
    List.append(z)
print (List, '- список')

max=List[0]
min=List[0]
for k in List:
    if max<k:
        max=k
    if min>k:
        min=k
# ищем индексы мин. и макс. элементов
index_max=List.index(max)
index_min=List.index(min)
# выводим мин и макс и их индексы
print('max =', max, '( index:', index_max, ')', ',', 'min =', min, '( index:', index_min, ')')
# меняем мин и макс местами
List[index_max], List[index_min] = List[index_min], List[index_max]
# опять ищем их индексы
index_max, index_max = index_min, index_max
# пустая строка
print()
# выводим результат
print (tuple(List), ' - результат')
# опять выводим мин и макс с их индексами
print('max =', max, '( index:', index_min, ')', ',', 'min =', min, '( index: ', index_max, ')')




