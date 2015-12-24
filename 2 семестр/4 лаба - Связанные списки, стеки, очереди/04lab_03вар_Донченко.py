# 3. Реалізувати клас однонаправлений зв’язаний список,
# який містив би наступні методи:
# addLast(e) – додає елемент у кінець списку
# takeLast() – видаляє та повертає останній елемент зі списку
# І на основі цього класу реалізувати клас стек (Stack),
# у середині якого буде використовуватись зв’язаний список



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

    def takeLast(self):
        if self.head == None: # если нет 1-го элемента (список пустой)
          return
        old = curr = self.head
        index_count = 0
        while curr != None:
            if index_count == self.length-1:
                old.next = curr.next
                self.tail = old
                self.length -= 1
                return str(curr)
            old = curr  
            curr = curr.next
            index_count += 1


class Stack(object):

    def __init__(self):
        self.items = LinkedList()

    def __str__(self):
        return str(self.items)

    def push(self, item):
        self.items.addLast(item)

    def pop(self):
        return self.items.takeLast()

    def is_empty(self):
        return self.items.length==0




        
