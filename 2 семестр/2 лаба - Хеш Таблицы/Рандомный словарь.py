# Задание:
# 1) вводим кол-во "ключ-значение"
# 2) ключ - строка длиной от 1 до 10 символов
# 3) значение - любое число от 0 до 1000

from random import randint

# KEY
def new_value(x = ''):
    for K in range(randint(1,10)):
        x += chr(randint(40,125))
    return x

SizeOfDictionary = int(input('Размер словаря: '))
Dictionary = {randint(1,1000) : new_value()  for E in range(SizeOfDictionary)}

print(Dictionary)
