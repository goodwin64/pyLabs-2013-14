# 6. Допоможіть інтернет-крамниці! Крамниція має звязок
# з соціальною мережею, і коли хотось купує в ній якийсь товар,
# то ця інформація зберігається в описі користувача.
# Використовуючи пошук в ширину, розробіть сервіс рекомендацій
# для інтернет-крамниці. Він має визначати, чи рекомендувати
# певний товар користувачеві, якщо його придбало більше 50%
# його друзів та більше 70% друзів його друзів.

from random import randint
from Lec8_Graph import Graph, Vertex

NameList = ['Ваня', 'Макс', 'Стёпа', 'Игорь', 'Жека', 'Серега']
SurnameList = ['Стасюк', 'Донченко', 'Конюхов', 'Лавровский', 'Шпак']
idList = [x for x in range(1, 1001)] # 1к пользователей в соц. сети 



class SocialNetworkUser(object):
    '''Пользователь соц. сети'''

    def __init__(self, name, surname, id_number):
        #Vertex.__init__(self, id_number)
        self.name = name
        self.surname = surname
        self.data = (self.name, self.surname)
        self.id = id_number
        self.vertex = Vertex(id_number)
        
    def __str__(self):
        return '%s %s, (id=%d) is connectedTo %s' % (self.name, self.surname, self.id, str([x.id for x in self.vertex.connectedTo]))

    def new_friend(self, Friend):
        self.vertex.addNeighbor(Vertex(Friend.id), 1)
        Friend.vertex.addNeighbor(Vertex(self.id), 1)

    def print_friends(self):
        print( 'Друзья %s (id=%s):\n %s' % (self.data,\
                                               self.id,\
                                              [x.id for x in self.vertex.connectedTo]))

    def friends(self):
        return self.vertex.getConnections()
        
    def friends_in_degree(self, Degree_of_Friendship):
        FF_list = set() # временный список друзей пользователя N-ного порядка
        pass ################## <-----------------------------------------------

    def degree_of_friendship(self, Person):
        if Person in self.friends():
            return 1
        else:
            return degree_of_friendship(self.friends(), Person) + 1
##        return self.vertex.getWeight(self, Friend)



class Customer(SocialNetworkUser):
    
    def __init__(self, ID_number):
        SocialNetworkUser.__init__(self, ID_number)
##        self.id = ID_number
##        self.name = Base_of_Users [self.id] [0]
##        self.surname = Base_of_Users [self.id] [1]
##        self.FriendList = Base_of_Users [self.id] [2]
##        self.data = Base_of_Users [self.id]
        self.ShopList = []
        Base_of_Users[self.id].append(self.ShopList)

    def __str__(self):
        return 'Клиент {0}, id={1}, друзья:\n{2}\nПокупки:\n{3}'.format(self.data[0:2], self.id, self.data[2], self.data[3])

    def new_purchase(self, Purchase):
        self.ShopList.append (Purchase)
        return '{} купил {}'.format((self.name, self.surname), Purchase)

    def whether_to_buy(self, Purchase):
        condition1 = False
        condition2 = False
        
        Count_of_this_Purchase = 0 # флаг на к-тво продаж этого товара
        for Friend in self.FriendList: # проход по списку друзей
            if Purchase in Base_of_Users [ Friend[2] ] [3]: # если товар есть в списке покупок друга
                Count_of_this_Purchase += 1 # ставлю +1
        if Count_of_this_Purchase >= len(self.FriendList)*0.5: # не менее 50% друзей купили этот товар
            condition1 = True # условие 1 выполняется
            
        Count_of_this_Purchase = 0 # снова флаг на к-тво продаж этого товара
        for ID in self.friends_friends(): # по множеству id друзей друзей
            if Purchase in Base_of_Users [ID] [3]: # если товар есть в списке покупок этого человека
                Count_of_this_Purchase += 1
        if Count_of_this_Purchase >= len(self.friends_friends())*0.7: # не менее 70% друзей друзей
            condition2 = True # условие 1 выполняется

        if condition1 == True and condition2 == True:
            return True
        return False


        
class SocialNetwork(Graph):
    '''Класс СОЦ.СЕТЬ на основе класса Граф'''

    def __init__(self):
        self.usersList = {}
        self.usersCount = 0

    def addUser(self,key):
        self.usersCount += 1
        newUser = Vertex(key)
        self.usersList[key] = newUser
        return newUser

    def getUser(self,n):
        if key in self.usersList:
            return self.usersList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.usersList

    def addEdge(self,f,t,cost=0):
        if f not in self.usersList:
            nv = self.addUser(f)
        if t not in self.usersList:
            nv = self.addUser(t)
        fr = self.usersList[f]
        to = self.usersList[t]
        fr.addNeighbor(to, cost)
        #self.usersList[f].addNeighbor(self.usersList[t], cost)

    def getVertices(self):
        return self.usersList.keys()

    def __iter__(self):
        return iter(self.usersList.values())




# Пользователи: (тест)
a = SocialNetworkUser (NameList [randint(0,5)],\
                SurnameList [randint(0,4)],\
                 randint(0,1000))
del idList[idList.index(a.id)]

b = SocialNetworkUser(NameList [randint(0,5)],\
                SurnameList [randint(0,4)],\
                 randint(0,1000))
del idList[idList.index(b.id)]

c = SocialNetworkUser(NameList [randint(0,5)],\
                SurnameList [randint(0,4)],\
                 randint(0,1000))
del idList[idList.index(c.id)]

d = SocialNetworkUser(NameList [randint(0,5)],\
                SurnameList [randint(0,4)],\
                 randint(0,1000))
del idList[idList.index(d.id)]

e = SocialNetworkUser(NameList [randint(0,5)],\
                SurnameList [randint(0,4)],\
                 randint(0,1000))
del idList[idList.index(e.id)]

f = SocialNetworkUser(NameList [randint(0,5)],\
                SurnameList [randint(0,4)],\
                 randint(0,1000))
del idList[idList.index(f.id)]


# Добавление в друзья (тест)
a.new_friend(b)
a.new_friend(c)
b.new_friend(e)
d.new_friend(c)
c.new_friend(f)
# "b" и "c" - не друзья
# У пользователя А: друзей 2 (B, C), друзей друзей 4 (A, D, E, F)






