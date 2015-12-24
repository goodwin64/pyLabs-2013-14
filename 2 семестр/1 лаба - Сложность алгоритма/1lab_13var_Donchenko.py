# 13. Напишите программу, которая вводит с клавиатуры два непустых
# неубывающих списка целых чисел, и печатает те и только те элементы,
# которые входят только в один из списков (симметрическая разность множеств).

# Для каждого элемента из списка меньшей длины юзаем проверку
# наличия этого числа в другом списке через бинарный поиск,

import random

def puzirjok(arr): # сортировка "пузырьком"
    i = len(arr)
    while i > 1:
       for j in range(i - 1):
           if arr[j] > arr[j + 1]:
               arr[j], arr [j+1] = arr [j+1], arr [j]
       i -= 1

def binary_search(x, List):
    i = 0 # первый элемент
    j = len(List)-1 # последний элемент
    m = int(j / 2) # середина (приблизительно)
    # пока искомое значение не равно текущей середине
    # или левая граница зашла за правую (элемент не найден)
    while List[m]!=x and i <= j: 
        if x > List[m]: # если значение больше серединного(левая половина)
            i = m+1 # переместить левую границу до середины
            
            m = int((i+j)/2)
        elif x < List[m]: # справа от середины
            j = m-1 # то сместить правую границу за середину
            m = int(j / 2) # найти новую середину
    if i > j:
        return False
    else:
        return m+1
    

# Переменные

Array1 = []
Array2 = []
Array1_unique = [] #
Array2_unique = [] #

print()

# Параметры списков
SizeOfArray1 = int(input('Кількість елементів першого списку: '))
for k in range(SizeOfArray1):
    z = int(input('element: '))
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

for E in Array1:
    if binary_search(E, Array2) == False:
        Array1_unique.append(E)
for E in Array2:
    if binary_search(E, Array1) == False:
        Array2_unique.append(E)

print()
print('Элементы, которые есть только в 1 списке:')
print(Array1_unique)
print()
print('Элементы, которые есть только в 2 списке:')
print(Array2_unique)







    
