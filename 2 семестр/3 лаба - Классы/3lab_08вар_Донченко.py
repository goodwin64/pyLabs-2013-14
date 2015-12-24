# Задание 8
# Створити class Студент (Student), який би мав:
# ---> конструктор, що задає прізвище та ім’я, а також словник, де у якості
# ключа буде значитись семестр, значеннями буде список оцінок за цей семестр
# ---> метод __str__ для перетворення на рядок для використанні у функції print
# ---> метод для обчислення середнього балу за певний семестр
# ---> метод для обчислення середнього балу за всі роки навчання
# ---> метод, який би задавав список оцінок за певний семестр
# ---> метод, який би повертав список оцінок за певний семестр

from random import randint # использую рандом для оценок студентов
# У каждого оценки от 3 до 5, количество предметов от 4 до 8

def Average_number(List):
    if len(List) != 0:
        return round( sum(List)/len(List), 1)
    return 'Пустой список'

First_student_marks = {1:[randint(3,5) for x in range(randint(4,8))],
     2:[randint(3,5) for x in range(randint(4,8))],
     3:[randint(3,5) for x in range(randint(4,8))]} # Оценки студента 1
print('First_student_marks - словарь оценок 1-го студента:')
for E in sorted(First_student_marks.keys()):
    print('{0} семестр: {1}'.format(E, First_student_marks[E]))
          
Second_student_marks = {1:[randint(3,5) for x in range(randint(4,8))],
     2:[randint(3,5) for x in range(randint(4,8))],
     3:[randint(3,5) for x in range(randint(4,8))]} #Оценки студента 2
print('Second_student_marks - словарь оценок 2-го студента:')
for E in sorted(Second_student_marks.keys()):
    print('{0} семестр: {1}'.format(E, Second_student_marks[E]))

class Student(object):
    
    def __init__(self, surname, name, Dictionary):
        self.surname = surname
        self.name = name
        self.Dictionary = Dictionary
        
    def __str__(self):
        '''Перегрузка принта'''
        return "Студент {0} {1}".format(self.surname, self.name)

    def average_mark_in_semester(self, Sem):
        '''Средний балл за определенный семестр'''
        List_of_marks_in_this_semester = self.Dictionary[Sem] # список оценок за семестр Sem
        Average_mark = Average_number(List_of_marks_in_this_semester) # средний балл
        return Average_mark

    def average_mark_in_all_semesters(self):
        '''Средний балл за все семестры'''
        List_of_marks = []
        for Lists_of_marks in self.Dictionary.values():
            for Mark in Lists_of_marks:
                List_of_marks.append(Mark)
        Average_mark = Average_number(List_of_marks) # средний балл
        return Average_mark

    def edit_marks_in_semester(self, Sem):
        '''Изменение оценок в определенном семестре'''
        self.Dictionary[Sem] = list (map(int, input('Введите новые оценки через пробел: ').split()))

    def show_marks_in_semester(self, Sem):
        '''Показывает оценки за определенный семестр'''
        return self.Dictionary[Sem]
