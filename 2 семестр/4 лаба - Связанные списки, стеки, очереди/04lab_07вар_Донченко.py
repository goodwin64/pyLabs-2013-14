# 7. Для математичного виразу представленого як рядок,
# у вигляді постфіксної нотації (зворотній польський запис),
# реалізуйте метод для обчислення значення цього виразу
# з використанням стеку. Операції, які повинні оброблятись: +, -, *, /
# Приклад запису виразу "5 + ((1 + 2) * 4) − 3"
# у польській нотації: 5 1 2 + 4 * + 3 –
  
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
    
################################ПРОВЕРКА №1
def if_all_OK_with_brackets(expr):
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
                    print("После скобки {0} не идет закрывающая для нее\n".format(last))
                    return False
                elif symb == anti (last):
                    stack.pop()
            else: # если стек пуст
                print("Для скобки {} нет открывающей\n".format(symb))
                return False
    if stack.is_empty() == False:
        print("Открывающих больше, чем закрывающих\n")
        return False
    print("Ошибок нет\n")
    return True

################################ПРОВЕРКА №2
def check_brackets(expression):#проверка на баланс скобок
    bracketsAmount=0            #счетчик скобок
    for symbol in expression:   #цикл по каждому символу
        if bracketsAmount==-1:  #если счетчик скобок равен -1, значит закрывающая скобка стоит раньше открывающей
            return False        #а это неправильно,возвращаем фолс
        if symbol=='(':         #если символ равен открывающей скобке, прибавляем к счетчику 1
            bracketsAmount+=1
        elif symbol==')':       #если символ равен закрывающей скобке, вычитаем единицу из счетчика
            bracketsAmount-=1
    if bracketsAmount!=0:
        #после того как все выражение пройдено, смотрим: если счетчик скобок не равен нулю,
        #значит у нас дисбаланс скобок
        return False            #возвращаем фолс
    return True                 #если все нормально возвращаем тру

 
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
 
 
def operations(): # возвращает допустимые операции
    return '"+" - сложение\n"-" - вычитание\n"*" - умножение\n"/" - деление\n"^" - возведение в степень'
 
def calculate(expression): #функция вычисления выражения,передаваемого в обратной польской записи
    stack = []; #стэк(список) для хранения чисел
    number='';  #строка в которую будем записывать число, затем преобразовывать его в int , и очищать эту строку, и так с каждым числом
    iter=0
    if expression=='': #если ниче не ввели то возвращаем что все плохо
        return 'Ошибка при вычислении.Проверьте корректность данного выражения'
    for symbol in expression: #идем по строке в которой выражение
        if symbol=='-':       #если символ равен "-"
            try:              #пробуем посмотреть следующий символ
                if expression[iter+1]in allowed_nums():     #смотрим ,если следующий символ после минуса число
                    number+=symbol                          #то записываем минус в строку , которая будет числом (строка ,потому что число может быть отрицательным и двузначным)
                    iter+=1
                    continue                                #переходим к следующему шагу цикла
            except IndexError:      #если не получается посмотреть,значит этот минус последний символ в строке,а следовательно он не может принадлежать числу,значит он оператор
                pass                #пропускаем и идем дальше
        if symbol in allowed_nums():      #если символ - число
            number+=symbol                #то записываем его в строку, в которой будет формироваться число
            iter+=1
            continue                      #переходим к следующему шагу цикла
        if number!='':                    #если в строке,формирующей число что-то есть
            num=float(number)               #то преобразуем это число в float
            stack.append(num)             #и записываем его в стэк
            number=''                     #строку очищаем
        if not symbol in AllowedOperators.keys():       #если символ не оператор
            iter+=1
            continue
        try:
            number2=stack.pop()
            number1=stack.pop()
        except IndexError:
            return 'Количество операторов должно быть меньше количества операндов на 1. Возможно вы ввели минус слитно с числом';
        try:
            result=AllowedOperators[symbol](number1,number2)
            #print str(number1)+' '+symbol+' '+str(number2);
        except ZeroDivisionError:
            return 'Ошибка: деление на 0'
        iter+=1
        stack.append(result);
    if len(stack)!=1:
        return 'Количество операторов должно быть меньше количества операндов на 1. Возможно вы ввели минус слитно с числом';
    res=str(stack.pop())
    return 'Преобразованное в ОПЗ выражение: '+expression+'\nОтвет: '+str(res);
 
 
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

print ('Калькулятор производит операции только с ЦЕЛЫМИ ЧИСЛАМИ!')
print ('При вводе отрицательного числа вводите знак минус ТОЛЬКО СЛИТНО с числом!\n')
print ('Допустимы следующие операции:')
print (operations())
print ('Введите выражение:')
while True:
    expression = (input('>>> '));
    while not check_symbols(expression):
        print ('Вы ввели недопустимые символы! Повторите ввод')
        expression = (input('>>> '));
    if check_brackets(expression):
        print (str(calculate(return_Polish_record(expression))))
    else:
        print ('Ошибка. Проверьте правильность ввода скобок')
