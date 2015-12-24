# 1) Знайти мінімальне та максимальне значення
# у списку довільної довжини. Створити кортеж, який
# буде містити ці значення та матиме наступний вигляд:
# ((min_value, min_index), (max_value, max_index))

import random

# Размер дальнейшего списка
SizeOfArray=int(input('Введіть розмір подальшого списку - кількість елементів у ньому: '))
# На случай, если введено целое, но отрицательное

# наш список
List=[]
TupOfMax=[]
TupOfMin=[]
FinalTup=[]

# аппенд - добавляет к списку на последнюю позицию элемент и каждый раз на единичку больше
for k in range(1, SizeOfArray+1):
    z=(random.randint(-100, 100)) # работа random'a только с целыми числами
    List.append(z)
print('SPISOK: ')
print(List)
index=0
# работа с минимальным в массиве элементов
min=List[index]
for k in List:
    if k<min:
        min=k
        break
    index+=1
TupOfMin.append(min)
TupOfMin.append(index)
TupOfMin=tuple(TupOfMin)
index=0
# работа с максимальным в массиве элементов
max=List[index]
for k in List:
    if k>max:
        max=k
        break
    index+=1
TupOfMax.append(max)
TupOfMax.append(index)
TupOfMax=tuple(TupOfMax)
# итог
FinalTup.append(TupOfMin)
FinalTup.append(TupOfMax)

print (tuple(FinalTup))

#
#
#
#
#
#
#
#
