##########################################################################################код
class Node:
        def __init__(self, name):
                self.connected={}
                self.name=name
                self.waynum=0
        def ConnectWith(self, other):
                self.connected[other.name]=other
                other.connected[self.name]=self
class Graf:
        def __init__(self):
            self.elements={}
        def addElem(self,e):
            self.elements[e]=Node(e)
        def connect(self,a,b):
            self.elements[a].ConnectWith(self.elements[b])
        def helpfunc(self,a, b, way=dict()):
            way2=dict()
            for k in list(way.keys()):
                way2[k]=None
            if a==b:

                print(list(way))
                self.elements[b].waynum+=1
            for i in list(self.elements[a].connected.keys()):
                way2[a]=None
                if i not in way2:
                    self.helpfunc(i,b,way2)
        def  WayCount(self,a,b):
                print('|(Для проверки)пути снизу:(порядок не верный)')
                self.helpfunc(a,b)
                a=self.elements[b].waynum
                self.elements[b].waynum=0
                return a
        def __str__(self):
                return str(list(self.elements.keys()))
######################################################################################проверка
A=Graf()
for i in range(1,11):
        A.addElem(i)
A.connect(1,2)
A.connect(1,3)
A.connect(2,4)
A.connect(2,5)
A.connect(3,5)
A.connect(3,6)
A.connect(4,7)
A.connect(4,8)
A.connect(5,8)
A.connect(5,9)
A.connect(6,9)
A.connect(6,10)
print(A.WayCount(1,3))

