# Задание 3:
# Реалізувати class Точка (Point) (задається двома координатами), і на її основі
# class Лінія (Line). Клас лінія з наступними методами:
# ---> конструктор, що задає координати лінії двома точками типу класу Point
# ---> метод __str__ для перетворення на рядок для використанні у функції print
# ---> метод для знаходження довжини лінії
# ---> метод, який би повертав точку (Point), яка знаходиться на середині лінії
# ---> метод, який повертає довжину проекції на вісь Х
# ---> метод, який повертає довжину проекції на вісь Y

from math import sqrt

class Point:
    ''' Класс "точка" '''
    
    def __init__(self, x, y):
        '''Создание новой точки.'''
        self.x = x
        self.y = y
        
    def __str__(self):
        '''Вывод координат x, y точки.'''
        return " ({0}, {1})".format(self.x, self.y)

class Line:
    ''' Класс "линия" '''

    def __init__(self, StartPoint, FinishPoint):
        self.Start = StartPoint
        self.Finish = FinishPoint
        
    def __str__(self):
        return "(Линия из точки {0} в точку {1})".format(self.Start, self.Finish)

    # Перегруженный __len__ выводит только целые числа,
    # поэтому использую метод .length()
    #def __len__(self):
    def length(self):
        '''Длина линии'''
        self.x = self.Finish.x - self.Start.x
        self.y = self.Finish.y - self.Start.y
        return round (sqrt( (self.x)**2 + (self.y)**2 ), 3)

    def middle(self):
        self.Mx = (self.Start.x + self.Finish.x) / 2 # координаты середины линии
        self.My = (self.Start.y + self.Finish.y) / 2
        return 'Середина линии: ({0}, {1})'.format(self.Mx, self.My)

    def x_proection(self):
        return abs (self.Finish.x - self.Start.x)

    def y_proection(self):
        return abs (self.Finish.y - self.Start.y)
