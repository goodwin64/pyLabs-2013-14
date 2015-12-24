class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

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
        if index < 0 or index > self.length: return
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

    def __str__(self):
        node = self.head
        string = ''
        while node:
            string += str(node) + ' '
            node = node.next
        return string

L = LinkedList()
L.addLast(1)
L.addLast(2)
L.addLast(5)
L.addFirst(0)
L.add(0, -1)
L.add(5, 6)
L.add(4, 3)
print L