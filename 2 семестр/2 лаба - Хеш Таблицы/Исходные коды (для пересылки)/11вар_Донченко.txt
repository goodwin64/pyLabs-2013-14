# Задание 11:
# Дан список состоящий из кортежей, где в кортеже указано
# имя и город, вида [('Andrii', 'Kyiv'), ('Nik', 'London'), ('Luba', 'Kyiv')].
# Выведите информацию сколько людей живет в каждом городе

def Make_a_list_of_tuples(string, separator='-'):
    List_of_tuples = string.split(',')
    for E in range(len(List_of_tuples)):
        tup = tuple(List_of_tuples[E].split(separator))
        List_of_tuples[E] = tup
    return List_of_tuples

def Make_a_dict_City_count(List):
    D = {}
    for Tuple in List:
        if Tuple[1] not in D:
            D[Tuple[1]] = 1
        else:
            D[Tuple[1]] += 1
    return D

# Start_string = input('Кто где живет?\n')
Start_string = '''Костя - Одесса, Влад - Кривой Рог, Игорь - Смела,
Магомет - Москва, Максим - Одесса, Игорь - Кривой Рог, Алик - Киев'''

List_of_tuples = Make_a_list_of_tuples(Start_string)
Dictionary = Make_a_dict_City_count(List_of_tuples)
for K in Dictionary.items():
    print('В городе {0} живет {1} людей'.format(K[0], K[1]))
