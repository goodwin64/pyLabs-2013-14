# Задание 6:
# Реалізувати class Точка (Point) (задається двома координатами)
# і на її основі class Вектор (Vector). Клас вектор з наступними методами:
# ---> конструктор, що задає координати початку та кінця вектора двома
# точками типу класу Point
# ---> метод __str__ для перетворення на рядок для використанні у функції print
# ---> метод для знаходження довжини вектора
# ---> метод, який би множив вектор на число
# ---> метод, який би виконував скалярне множення даного вектора на другий вектор

from math import sqrt

class Point:
    ''' Класс "точка" '''
    
    def __init__(self, x, y, z):
        '''Создание новой точки.'''
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        '''Вывод координат x, y, z точки.'''
        return " ({0}, {1}, {2})".format(self.x, self.y, self.z)

class Vector:
    ''' Класс "вектор" '''

    def __init__(self, StartPoint, FinishPoint):
        self.Start = StartPoint
        self.Finish = FinishPoint
        self.x = self.Finish.x - self.Start.x
        self.y = self.Finish.y - self.Start.y
        self.z = self.Finish.z - self.Start.z
        
    def __str__(self):
        ''' Координаты вектора'''
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)

    # Перегруженный __len__ выводит только целые числа,
    # поэтому использую метод .length()
    #def __len__(self):
    def length(self):
        '''Длина вектора'''
        return round (sqrt( (self.x)**2 + (self.y)**2 + (self.z)**2 ), 3)

    def mult(self, multiplier):
    #def __rmul__(self, multiplier):
        ''' Умножение вектора на скаляр (перегрузка не работает в 3.3)'''
        self.mX = multiplier * self.x
        self.mY = multiplier * self.y
        self.mZ = multiplier * self.z
        return "({0}, {1}, {2})".format(self.mX, self.mY, self.mZ)

    def skal_dobutok(self, vect2):
        return (self.x * vect2.x) + (self.y * vect2.y) + (self.z * vect2.z)
