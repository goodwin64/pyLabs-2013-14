# 6. Використовуючи стек написати перевірку правильності
# розстановки дужок ({, (, [ ), у деякому рядку.
# Наприклад “ab(cd{ef}gh[j])”
  
class Stack (object): 
    def __init__(self):
        self.items = []
    def push(self, item): # добавление на верхушку стека
        self.items.append(item)
        self.last = item
    def pop(self): # удаление последнего элемента
        return self.items.pop()
    def is_empty(self): # пустой ли стек
        return (self.items == [])

def is_open(symbol):
    if symbol == '(' or symbol == '[' or symbol == '{':
        return True
    
def anti(br): # противоположная скобка
    if br == '(':
        return ')'
    elif br == '[':
        return ']'
    elif br == '{':
        return '}'

def if_all_OK_with_brackets(expr):
    brackets_list = ['(', '[', '{', '}', ']', ')']
    stack = Stack()
    for symb in expr: # смотрю на каждый символ в выражении
        if symb not in brackets_list: # если это не скобка, пропускаю
            continue
        elif is_open(symb): # если это любая открывающая скобка, добавляю ее в стек
            stack.push(symb)
        else: # если закрывающая - смотрю на верхнюю в стеке
            if stack.is_empty() == False: # если в стеке что-то есть (тогда можно юзать pop)
                last = stack.pop() # последнюю скобку в стеке кладу в переменную last
                stack.push(last)
                if symb != anti (last):
                    # сравниваю, противоположна ли верхняя скобка в стеке для нее
                    print("После скобки {0} не идет закрывающая для нее\n".format(last))
                    return
                elif symb == anti (last):
                    stack.pop()
            else: # если стек пуст
                print("Для скобки {} нет открывающей\n".format(symb))
                return
    if stack.is_empty() == False:
        print("Открывающих больше, чем закрывающих\n")
        return
    print("Ошибок нет\n")
    return

while True:
    YourFrase = input("Введите Ваше выражение: ")
    if YourFrase == 'stop' or YourFrase == 'стоп':
        break
    if_all_OK_with_brackets (YourFrase)

