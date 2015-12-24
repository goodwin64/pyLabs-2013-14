# 10. На основі зв’язаного списку реалізуйте клас кільцевий буфер (RingBuffer)
# Методи:
# __init__(self, size=1) - задає розмір буферу
# add(e) – додає елемент, якщо в буфері є місце і повертає True,
# інакше повертає False
# take() – повертає елемент з буфера, якщо він є, інакше повертає None


class Node(object):
    ''' Один из узлов связного списка'''
    
    def __init__(self, cargo=None, Next=None):
        self.cargo = cargo # данные узла
        self.next = Next # ссылка на следующий узел связного списка
        
    def __str__(self):
        return str(self.cargo)

Dic = {}

    
class RingBuffer(object):
    '''Кольцевой буфер'''

    def __init__(self, size=1):
        self.current_index = 0
        self.items = 0
        self.head = None
        self.tail = None
        self.x = int(input('size: '))

    def add(self, index, e):
        Dic[index] = e
        node = Node(e)
        if self.items < self.x:
            if self.items == 0:
                self.head = node
                self.tail = node
            else:
                self.items+1 == self.x:
                self.tail.next = node
                self.tail = node
                if self.items+1 == self.x:
                    self.tail.next = self.head
            return True
        else:
            return False

    def take(self):
        







        
