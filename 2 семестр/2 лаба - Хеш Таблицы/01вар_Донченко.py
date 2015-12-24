# Задание 1:
# Дан список чисел. Определите, сколько раз в нем каждое из чисел встречается.

from random import randint

Array_of_numbers = [randint(1,10) for K in range(100)]
print(Array_of_numbers, '\n')
D = {}

for E in Array_of_numbers:
    if E not in D:
        D[E] = 1
    else:
        D[E] += 1

Sorted_keys = sorted(D.keys())
for E in Sorted_keys:
    print(E, 'встречается', D[E], 'раз')
