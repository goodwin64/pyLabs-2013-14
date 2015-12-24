#3) Дани два вектори a  =  (ax, ay, az) та b  =  (bx, by, bz). Знайти їх суму,
# скалярний та векторний добуток, а також норму кожного з них і кут між ними.

# Сразу пояснение: если пространство 3х - мерное, то нормалей у каждого
# вектора бесконечно много, поэтому я их не пишу

################# Импорт нужных библиотек

import random
from math import sqrt, acos, degrees

################# Заготовочки

Coordinates_a = []
Coordinates_b = []
Coordinates_c = []
mod_a=0
mod_b=0
Skal_dob = 0 # скалярное произведение  -  вектор D = ab
Kut = 0 # угол между векторами

################# Промежуточные действия

# аппенд  -  добавляет к списку на последнюю позицию элемент
for k in range(3):
    a = (random.randint( - 10, 10))
    b = (random.randint( - 10, 10))# работа random'a только с целыми числами
    Coordinates_a.append(a)
    Coordinates_b.append(b)
print('A: ', tuple(Coordinates_a))
print('B: ', tuple(Coordinates_b))

for k in range(3):
    orta_a = Coordinates_a[k] ** 2
    mod_a += orta_a
    orta_b = Coordinates_b[k] ** 2
    mod_b += orta_b
mod_a = sqrt(mod_a) # |a|
mod_b = sqrt(mod_b) # |b|


################# Решение и вывод ответов на экран

### Summa

for k in range(3):
    c = Coordinates_a[k] + Coordinates_b[k]
    Coordinates_c.append(c)
print('Сумма векторів a + b = c', tuple(Coordinates_c))



### skal dob

for k in range(3):
    Skal_dob += Coordinates_a[k] * Coordinates_b[k]
print('Cкалярний добуток векторів a*b=d=', Skal_dob)



### ugol

Cos_ab = Skal_dob / (mod_a * mod_b) # cos(a,b)
ugol=degrees(acos(Cos_ab))
print('Кут між векторами А і В: ', round(ugol, 1), '°')



### vect

Sin_ab = sqrt(1-Cos_ab**2) # sin(a,b)
Vect_dob = mod_a * mod_b * Sin_ab # векторное произведение E=[axb]=|a|*|b|*sin(a,b)
print('Векторний добуток векторів [a*b]=e=', round(Vect_dob, 1))









