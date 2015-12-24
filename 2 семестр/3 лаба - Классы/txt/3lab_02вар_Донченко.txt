# Задание 2:
# Створити class Комплексне число (Complex), який би мав:
# ---> конструктор, що задає значення числа у тригонометричній формі:
# через модуль і аргумент
# ---> метод __str__ для перетворення на рядок для використанні у функції print
# ---> перевантажений оператор «+» для додавання до поточного комплексного
# числа іншого комплексного числа
# ---> перевантажений оператор «-» для віднімання від поточного комплексного
# числа іншого комплексного числа
# ---> перевантажений оператор «*» для множення поточного комплексного числа
# на інше комплексне число
# ---> перевантажений оператор «/» для ділення поточного комплексного числа на
# інше комплексне число
# ---> метод для знаходження модуля комплексного числа

from math import sin, cos, degrees

class Complex:
    ''' Класс "Комплексное число" '''
    
    def __init__(self, z, angle):
        self.x = z * cos ( degrees (angle) )
        self.y = z * sin ( degrees (angle) )
        self.abs = z
        
    def __str__(self):
        result_x = round (self.x, 1)
        result_y = round (self.y, 1)
        return "Комплексное число ({0} , {1})".format(result_x, result_y)

    def __add__(self, other):
        result_x = round (self.x + other.x, 1)
        result_y = round (self.y + other.y, 1)
        return '({0} , {1})'.format(result_x, result_y)

    def __sub__(self, other):
        result_x = round (self.x - other.x, 1)
        result_y = round (self.y - other.y, 1)
        return '({0} , {1})'.format(result_x, result_y)

    def __mul__(self, other):
        result_x = round (self.x * other.x, 1)
        result_y = round (self.y * other.y, 1)
        return '({0} , {1})'.format(result_x, result_y)

    def __truediv__(self, other):
        if other.x != 0 and other.y != 0:
            result_x = round (self.x / other.x, 1)
            result_y = round (self.y / other.y, 1)
            return '({0} , {1})'.format(result_x, result_y)
        return 'Координаты второго числа не должны равняться нулю'

    def module(self):
        return self.abs
