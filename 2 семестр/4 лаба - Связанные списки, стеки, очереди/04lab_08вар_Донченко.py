# 8. На основі приведеного за посиланням алгоритму, реалізуйте
# перетворення вхідного виразу в постфіксну нотацію
# (зворотній польський запис)
# Приклад запису вхідного виразу "5 + ((1 + 2) * 4) - 3".
# Результат роботи програми перетворення у постфіксну
# нотацію: “5 1 2 + 4 * + 3 -“
  
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

def all_OK_with_brackets(expr):
    brackets_list = ['(', '[', '{', '}', ']', ')']
    stack = Stack()
    for symb in expr: # смотрю на каждый символ в выражении
        if symb not in brackets_list: # если это не скобка, пропускаю
            continue
        elif is_open(symb): # если это любая открывающая скобка, добавляю ее в стек
            stack.push(symb)
        else: # если закрывающая - смотрю на верхнюю в стеке
            if stack.is_empty()==False: # если в стеке что-то есть (тогда можно юзать pop)
                last = stack.pop() # последнюю скобку в стеке кладу в переменную last
                stack.push(last)
                if symb != anti (last):
                    # сравниваю, противоположна ли верхняя скобка в стеке для нее
                    return False
                elif symb == anti (last):
                    stack.pop()
            else: # если стек пуст
                return False
    if stack.is_empty() == False:
        return False
    return True

 
AllowedOperators = { #словарь(ассоциативный массив) операторов
    '-':float.__sub__, #определяю ключи к операторам, и действия которые они выполняют
    '+':float.__add__,
    '*':float.__mul__,
    '/':float.__truediv__,
    '^':float.__pow__,
}
 
Priority = {#словарь приоритетов операторов (по убыванию)
    '^':4,
    '*':3,
    '/':3,
    '+':2,
    '-':2,
    '(':1,
}

 
def check_symbols(expression): #функция проверяет введенное выражение на корректность
    allowed_symbols=set('0123456789-+*/ ().^'); #разрешимые символы для ввода
    if set(expression).issubset(allowed_symbols): #если в expression нет никаких других символов кроме разрешенных
        return True; #возвращаем,что все нормально
 
 
def allowed_nums(): #возвращает разрешимые ЦИФРЫ
    return '0123456789.'
 
 
def return_Polish_record(expression):
    isSearch=False
    stack = []
    outstring=''
    iter=0
    for symbol in expression:
        if symbol=='-':
            try:
                if expression[iter+1] in allowed_nums():
                    outstring+=symbol
                    iter+=1
                    continue
            except IndexError:
                pass
        if symbol==')':
            i=0
            for elem in stack:
                if elem=='(':
                    pos=i
                i+=1
            if pos<len(stack):
                stack.pop(pos)
            k=len(stack)
            while k>pos:
                outstring+=stack.pop()
                k-=1
            outstring+=' '
        if symbol in allowed_nums():
            try:
                if expression[iter+1] in allowed_nums():
                    outstring+=symbol
                else:
                    outstring+=symbol+' '
            except IndexError:
                outstring+=symbol+' '
        if symbol=='(':
            stack.append(symbol)
            outstring+=' '
        if symbol in AllowedOperators.keys():
            if not stack:
                stack.append(symbol)
            else:
                if Priority[symbol]>Priority[stack[-1]]:
                    stack.append(symbol)
                else:
                    cnt=0
                    for elem in stack:
                        if elem=='(':
                            while cnt<len(stack):
                                if Priority[stack[cnt]]>=Priority[symbol]:
                                    outstring+=stack.pop(cnt)+' '
                                cnt+=1
                            stack.append(symbol)
                            isSearch=True
                            break
                        cnt+=1
                        if not isSearch:
                            for elem in stack:
                                if Priority[elem]>=Priority[symbol]:
                                    i=0
                                    while stack[i]!=elem:
                                        i+=1
                                    outstring+=stack.pop(i)+' '
                            stack.append(symbol)
        iter+=1
    for elem in reversed(stack):
        outstring+=elem+' '
    return outstring

print ('Введите выражение:')
while True:
    expression = (input('>>> '));
    while not check_symbols(expression):
        print ('Вы ввели недопустимые символы! Повторите ввод')
        expression = (input('>>> '));
    if all_OK_with_brackets(expression):
        print (str(return_Polish_record(expression)))
    else:
        print ('Ошибка. Проверьте правильность ввода скобок')
