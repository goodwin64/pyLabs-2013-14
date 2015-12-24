# 6. Допоможіть інтернет-крамниці! Крамниція має звязок
# з соціальною мережею, і коли хотось купує в ній якийсь товар,
# то ця інформація зберігається в описі користувача.
# Використовуючи пошук в ширину разробіть сервіс рекомендацій
# для інтернет-крамниці. Він має визначати, чи рекомендувати
# певний товар користувачеві, якщо його придбало більше 50%
# його друзів та більше 70% друзів його друзів.

from random import randint
from Lec8_Graph import Graph, Vertex
from Lec8_Queue import Queue
from Lec8_BFS import bfs

NameList = ['Ваня', 'Макс', 'Стёпа', 'Игорь', 'Жека', 'Серега']
SurnameList = ['Стасюк', 'Донченко', 'Конюхов', 'Лавровский', 'Шпак']
idList = [x for x in range(1, 1001)] # 1к пользователей в соц. сети
Base_Of_Users = {} # база данных соц. сети





class FaceBookUser(object):
    '''Пользователь соц. сети'''

    def __init__(self, name, surname, id_number):
        self.name = name
        self.surname = surname
        self.data = (self.name, self.surname)
        self.id = id_number
        Base_Of_Users [self.id] = self.data # ID:ФИО
        self.vertex = Vertex(self.id)

    def __str__(self):
        return '{0} {1}, id={2}'.format(self.name, self.surname, self.id)

    def new_friend(self, Friend):
        self.vertex .addNeighbor (Vertex(Friend.id), 1)
        Friend.vertex .addNeighbor (Vertex(self.id), 1)

    def friends(self):
        print( 'Друзья {0}(id={1}):\n {2}'.format(Base_Of_Users [self.id],\
                                               self.id,\
                                              [x.id for x in self.vertex.connectedTo]))
        
    def friends_degree(self, Degree_of_Friendship):
        FF_list = [] # временный список друзей пользователя N-ного порядка
        



    

class Customer(FaceBookUser):
    
    def __init__(self, ID_number):
        self.id = ID_number
        self.name = Base_of_Users [self.id] [0]
        self.surname = Base_of_Users [self.id] [1]
        self.FriendList = Base_of_Users [self.id] [2]
        self.data = Base_of_Users [self.id]
        self.ShopList = []
        Base_of_Users [self.id] .append (self.ShopList)

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
        





# Пользователи: (тест)
a = FaceBookUser (NameList [randint(0,5)],\
                SurnameList [randint(0,4)],\
                 randint(0,1000))
del idList[a.id]

b = FaceBookUser(NameList [randint(0,5)],\
                SurnameList [randint(0,4)],\
                 randint(0,1000))
del idList[b.id]

c = FaceBookUser(NameList [randint(0,5)],\
                SurnameList [randint(0,4)],\
                 randint(0,1000))
del idList[c.id]

d = FaceBookUser(NameList [randint(0,5)],\
                SurnameList [randint(0,4)],\
                 randint(0,1000))
del idList[d.id]

e = FaceBookUser(NameList [randint(0,5)],\
                SurnameList [randint(0,4)],\
                 randint(0,1000))
del idList[e.id]

f = FaceBookUser(NameList [randint(0,5)],\
                SurnameList [randint(0,4)],\
                 randint(0,1000))
del idList[f.id]


# Добавление в друзья (тест)
a.new_friend(b)
a.new_friend(c)
b.new_friend(e)
d.new_friend(c)
c.new_friend(f)
# "b" и "c" - не друзья
# У пользователя А: друзей 2 (B, C), друзей друзей 4 (A, D, E, F)






