# 1) Створити class Комплексне число (Complex), який би мав:
# ---> конструктор, що приймає дійсну та уявну частину (за замовченням вони
#рівні 0)
# ---> метод __str__ для перетворення на рядок для використанні у функції print
# ---> перевантажений оператор «+» для додавання до поточного комплексного
#числа іншого комплексного числа
# ---> перевантажений оператор «-» для віднімання від поточного комплексного
#числа іншого комплексного числа
# ---> перевантажений оператор «*» для множення поточного комплексного числа
#на інше комплексне число
# ---> перевантажений оператор «/» для ділення поточного комплексного числа на
#інше комплексне число
# ---> метод для знаходження модуля комплексного числа

from math import sqrt

class Complex(object):
    ''' Класс "Комплексное число" '''
    
    def __init__(self, Real, Imagine):
        self.x = Real
        self.y = Imagine
        
    def __str__(self):
        return "Комплексное число ({0} , {1})".format(self.x, self.y)

    def __add__(self, other):
        ''' Перегрузка сложения '''
        result_x = self.x + other.x
        result_y = self.y + other.y
        return '({0} , {1})'.format(result_x, result_y)

    def __sub__(self, other):
        ''' Перегрузка вычитания '''
        result_x = self.x - other.x
        result_y = self.y - other.y
        return '({0} , {1})'.format(result_x, result_y)

    def __mul__(self, other):
        ''' Перегрузка произведения '''
        result_x = round (self.x * other.x, 1)
        result_y = round (self.y * other.y, 1)
        return '({0} , {1})'.format(result_x, result_y)

    def __truediv__(self, other):
        ''' Перегрузка деления '''
        if other.x != 0 and other.y != 0:
            result_x = round (self.x / other.x, 1)
            result_y = round (self.y / other.y, 1)
            return '({0} , {1})'.format(result_x, result_y)
        return 'Координаты второго числа не должны равняться нулю'

    def module(self):
        return sqrt( self.x**2 + self.y**2 )
