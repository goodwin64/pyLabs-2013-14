# Задание 12:
# Дан список состоящий из кортежей, где в кортеже указано
# имя и город, вида [('Andrii', 'Kyiv'), ('Nik', 'London'), ('Luba', 'Kyiv')].
# Получите словарь, в котором ключами были бы города,
# а в качестве значений – списки, состоящие из имен людей,
# которые живут в данном городе.

def Make_a_list_of_tuples(string, separator='-'):
    List_of_tuples = string.split()
    for E in range(len(List_of_tuples)):
        tup = tuple(List_of_tuples[E].split(separator))
        List_of_tuples[E] = tup
    return List_of_tuples

def Make_a_dict_City_count(List):
    D = {}
    for Tuple in List:
        if Tuple[1] not in D:
            D[Tuple[1]] = [Tuple[0]]
        else:
            D[Tuple[1]].append(Tuple[0])
    return D

Start_string = input('Кто где живет?\n')

List_of_tuples = Make_a_list_of_tuples(Start_string)
Dictionary = Make_a_dict_City_count(List_of_tuples)
for K in Dictionary.items(): print(K)
