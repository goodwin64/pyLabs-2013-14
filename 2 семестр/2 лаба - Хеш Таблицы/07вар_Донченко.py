# Задание 7:
# Дан список чисел. Выведите числа,
# которые встречаются в списке только по одному разу.

from random import randint

def Unique_numbers(List):
    D = {}
    result = []
    for number in List:
        if number not in D:
            D[number] = [1, number]
        else:
            D[number][0] += 1
    for value in D.values():
        if value[0] == 1:
            result.append(value[1])
    print("\nУникальные числа:")
    return result

List = []

for E in range(int(input('Размер списка: '))):
    List.append(randint(1, 10))

print('\nСписок чисел: \n', List)

if len(List) != 0:
    print(Unique_numbers(List))
