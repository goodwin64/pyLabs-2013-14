# 1. Реалізувати клас однонаправлений зв’язаний список,
# який містив би наступні методи:
# ---> addFirst(e) – додає елемент у початок списку
# ---> addLast(e) – додає елемент у кінець списку
# ---> add(index, e) – додає елемент за вказаним індексом
# ---> takeFirst() – видаляє та повертає перший елемент зі списку
# ---> takeLast() – видаляє та повертає останній елемент зі списку
# ---> remove(index) – метод видаляє елемент за індексом та повертає його
# ---> set(index, e) – заміняє значення елемент у списку за вказаним індексом
# ---> get(index) – повертає значення елементу за вказаним індексом
# ---> sort() – виконує сортування списку алгоритмом сортування вставками


class Node(object):
    ''' Один из узлов связного списка'''
    
    def __init__(self, cargo=None, Next=None):
        self.cargo = cargo # данные узла
        self.next = Next # ссылка на следующий узел связного списка
        
    def __str__(self):
        return str(self.cargo)



    
class LinkedList(object):
    '''Связанный список'''

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __str__(self):
        node = self.head
        string = ''
        while node:
            string += str(node) + ' '
            node = node.next
        return string

    def addLast(self, e):
        node = Node(e)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def addFirst(self, e):
        node = Node(e)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def add(self, index, e):
        if index < 0 or index >= self.length: return
        if self.length == 0:
            self.addLast(e)
            return
        if index == 0:
            self.addFirst(e)
            return
        if index == self.length:
            self.addLast(e)
            return
        node = self.head
        i = 0
        while i < index-1:
            node = node.next
            i += 1
        newNode = Node(e, node.next)
        node.next = newNode

    def takeFirst(self):
        FirstElem = self.head
        if FirstElem == None:
            return None
        self.head = self.head.next
        if self.head == None:
            return None
        self.length -= 1
        return str(FirstElem)

    def takeLast(self):
        if self.head == None: # если нет 1-го элемента (список пустой)
          return
        old = curr = self.head
        index_count = 0
        while curr != None:
            if index_count == self.length-1: # значит это последний элемент
                old.next = curr.next
                self.tail = old
                self.length -= 1
                return str(curr)
            old = curr  
            curr = curr.next
            index_count += 1

    def remove(self, index):
        if self.head == None or index > self.length-1: # если нет 1-го элемента (список пустой)
          return
        old = curr = self.head
        current_index = 0
        if index == 0:
          self.takeFirst()
        if index == self.length-1:
          self.takeLast()
        while curr != None:
            if current_index == index:
              old.next = curr.next
              self.length -= 1
              return str(curr)
            old = curr  
            curr = curr.next
            current_index += 1

    def replace(self, index, e):
        if self.head == None or index > self.length-1: # если нет 1-го элемента (список пустой)
          return
        curr = self.head
        current_index = 0
        while curr != None:
            if current_index == index:
              curr.cargo = e
              return
            curr = curr.next
            current_index += 1

    def get_cargo_by_index(self, index):
        if self.head == None or index > self.length-1: # если нет 1-го элемента (список пустой)
          return
        curr = self.head
        current_index = 0
        while curr != None:
            if current_index == index:
              return curr.cargo
            curr = curr.next
            current_index += 1

    def changeMin_Max(self):
        if self.head == None:
            return
        index = 0
        curr = self.head
        Min = self.head
        Max = self.head
        while curr != None:
            if curr.cargo > Max.cargo:
                Max = curr
            if curr.cargo < Min.cargo:
                Min = curr  
            curr = curr.next
            index += 1
        Max.cargo, Min.cargo = Min.cargo, Max.cargo
        return self

    def Average(self):
        Summ = 0
        curr = self.head
        while curr != None:
            Summ += curr.cargo
            curr = curr.next
        return Summ/self.length
