#2) Знайти середнє арифметичне додатних та від’ємних
# значення у списку довільної довжини. Створити кортеж,
# який буде містити ці значення та матиме наступний вигляд:
# (sum_positive, sum_negative)

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
    z=(random.randint(-1000, 1000)) # работа random'a только с целыми числами
    List.append(z)

SumPos=0 # сумма положительных элементов
SumNeg=0 # сумма отрицательных
posCount=0 # количество положительных
negCount=0 # к-тво отрицательных
Final=[] # итоговый список, который будет потом кортежем

for k in List:
    if k>0:
        SumPos+=k
        posCount+=1
    elif k<0:
        SumNeg+=k
        negCount+=1

Final.append((round(SumPos/posCount), 1))
Final.append((round(SumNeg/negCount), 1))
print (tuple(Final))




