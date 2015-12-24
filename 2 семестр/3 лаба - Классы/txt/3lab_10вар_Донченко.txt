# Задание 10
# Створити class Викладач (Instructor), який би мав:
# ---> конструктор, що задає прізвище та ім’я, а також словник,
# де у якості ключа буде значитись семестр, значеннями буде
# список предметів на цей семестр
# ---> метод __str__ для перетворення на рядок для використанні у функції print
# ---> метод для обчислення кількості предметів на певний семестр
# ---> метод для обчислення середньої кількості предметів за всі семестри
# ---> метод, який би визначав у якому з семестрів було
# більше за все предметів у викладача
# ---> методи, які б дозволяли додавати/видaляти предмети у семестрах

First_Instructor_lessons = {1:["Матан", "ЛинАлгебра", "ТФКП"],
     2:["Матан", "ТФКП", "Биология"],
     3:["Физкультура", "Матан", "История", "English"]} # Предметы 1-го препода
print('First_Instructor_lessons - словарь предметов 1-го препода')
          
Second_Instructor_lessons = {1:["География"],
     2:["Литература", "Физика лабы", "Программирование"],
     3:["Геометрия", "История", "English"]} # Предметы 2-го препода
print('First_Instructor_lessons - словарь предметов 2-го препода')

class Instructor(object):
    
    def __init__(self, surname, name, Dictionary):
        self.surname = surname
        self.name = name
        self.Dictionary = Dictionary
        
    def __str__(self):
        '''Перегрузка принта'''
        return "Преподаватель {0} {1}".format(self.surname, self.name)

    def how_many_lessons_in_semester(self, Sem):
        return 'В {0} семестре у {1}и {2} предмета'.format(Sem, self.name[:-1], len(self.Dictionary[Sem]))

    def show_semester(self, Sem):
        return 'В {0} семестре у {1}и: {2}'.format(Sem, self.name[:-1], self.Dictionary[Sem])

    def average_count_of_lessons_in_all_semesters(self):
        '''Среднее к-тво предметов за все семестры'''
        count_of_lessons = 0
        for List_of_lessons in self.Dictionary.values():
            for Lesson in List_of_lessons:
                count_of_lessons += 1
        average_count_of_lessons = round( count_of_lessons/len(self.Dictionary), 1 )
        return 'У {0}и в среднем {1} предмета'.format(self.name[:-1], average_count_of_lessons)

    def in_which_semester_are_max_lessons(self):
        '''В каком семестре больше всего предметов'''
        Max = 0
        for E in self.Dictionary.keys():
            if len(self.Dictionary[E]) > Max:
                Max = E
        return 'У {0}и больше всего предметов в {1} семестре'.format(self.name[:-1], Max)

    def add_lessons_in_semester(self, Sem):
        '''Добавление предметов в определенный семестр'''
        self.Dictionary[Sem].append(input('Введите новые предметы через запятую: ').split(","))

    def delete_lessons_in_semester(self, Sem):
        '''Удаление предметов из определенного семестра'''
        Del_List = list (input('Какие предметы удалять? ').split(","))
        for E in Del_List:
            del self.Dictionary[Sem][self.Dictionary[Sem].index(E)]
