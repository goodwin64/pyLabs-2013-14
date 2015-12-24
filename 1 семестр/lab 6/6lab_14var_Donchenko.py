# 14) Дано список який містить набір результатів деяких
# вимірювань температури (як додатні, так і від’ємні значення).
# Знайти значення температури та її індекс, яка була ближча
# за все до 0. У результаті вивести кортеж, який містить
# значення температури найближчої до 0 та її індекс у списку.

from random import randint, random

A = tuple([round(randint(-10,10) + random(), 2) for x in range (20)])
result=[]
min_difference = abs(A[0])

for E in range(len(A)):
    if min_difference > abs(A[E]):
        min_difference = A[E]
        index = E
result.append(min_difference)
result.append(index)

print ('A:', A)
print(tuple(result))
