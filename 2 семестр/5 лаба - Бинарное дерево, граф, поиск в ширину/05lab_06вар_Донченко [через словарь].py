# 6. Допоможіть інтернет-крамниці! Крамниця має звязок
# з соціальною мережею, і коли хтось купує в ній якийсь товар,
# то ця інформація зберігається в описі користувача.
# Використовуючи пошук в ширину розробіть сервіс рекомендацій
# для інтернет-крамниці. Він має визначати, чи рекомендувати
# певний товар користувачеві, якщо його придбало більше 50%
# його друзів та більше 70% друзів його друзів.

from random import randint

NameList = ['Ваня', 'Макс', 'Стёпа', 'Игорь', 'Жека', 'Серега', 'Никита', 'Артем']
SurnameList = ['Стасюк', 'Донченко', 'Конюхов', 'Лавровский', 'Шпак', 'Маховец']
idList = [x for x in range(1, 1001)] # 1к пользователей в соц. сети
Base_of_Users = {} # База данных пользователей соц. сети





class FaceBookUser(object):
    '''Пользователь соц. сети'''

    def __init__(self, name, surname, id_number):
        self.name = name
        self.surname = surname
        self.id = id_number
        self.FriendList = []
        self.data = [name, surname, self.FriendList]
        Base_of_Users [self.id] =  self.data

    def __str__(self):
        return '{0} {1}, id={2}'.format(self.name, self.surname, self.id)

    def new_friend(self, Friend):
        self.FriendList.append( (Friend.name, Friend.surname, Friend.id) )
        Friend.FriendList.append( (self.name, self.surname, self.id) )

    def del_friend(self, Friend):
        del self.FriendList [self.FriendList.index((Friend.name, Friend.surname, Friend.id))]
        del Friend.FriendList [Friend.FriendList.index((self.name, self.surname, self.id))]

    def friends(self):
        print ('Друзья {}{}:'.format(self.name, self.surname))
        if len(self.FriendList) == 0:
            print('Отсутствуют\n')
        else:
            for friend in self.FriendList:
                print(friend[0:2], ', id =', friend[2]) # вывод только Имени, Фамилии и id (без данных)

    def friends_friends(self):
        FF_list = [] # временный список друзей друзей пользователя
        for Tuple_of_friends in Base_of_Users [self.id][2]: # кортеж каждого друга в списке друзей
            for Fr_Data in Base_of_Users [Tuple_of_friends [2]] [2]: # Данные каждого друга каждого друга
                FF_list.append(Fr_Data[2]) # в этом кортеже 3й элемент - id друга
        for n_counts in range(FF_list.count(self.id)):
            del FF_list[FF_list.index(self.id)]
        return set(FF_list)



    

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
a = FaceBookUser (NameList [randint(0,7)],\
                SurnameList [randint(0,5)],\
                 randint(0,len(idList)))
del idList[a.id]

b = FaceBookUser(NameList [randint(0,7)],\
                SurnameList [randint(0,5)],\
                 randint(0,len(idList)))
del idList[b.id]

c = FaceBookUser(NameList [randint(0,7)],\
                SurnameList [randint(0,5)],\
                 randint(0,len(idList)))
del idList[c.id]

d = FaceBookUser(NameList [randint(0,7)],\
                SurnameList [randint(0,5)],\
                 randint(0,len(idList)))
del idList[d.id]

e = FaceBookUser(NameList [randint(0,7)],\
                SurnameList [randint(0,5)],\
                 randint(0,len(idList)))
del idList[e.id]

f = FaceBookUser(NameList [randint(0,7)],\
                SurnameList [randint(0,5)],\
                 randint(0,len(idList)))
del idList[f.id]

g = FaceBookUser(NameList [randint(0,7)],\
                SurnameList [randint(0,5)],\
                 randint(0,len(idList)))
del idList[g.id]


# Добавление в друзья (тест)
a.new_friend(b)
a.new_friend(c)
b.new_friend(e)
d.new_friend(c)
c.new_friend(f)
g.new_friend(f)
# "b" и "c" - не друзья
# У пользователя А: друзей 2 (B, C), друзей друзей 4 (A, D, E, F)

A = Customer(a.id)
B = Customer(b.id)
C = Customer(c.id)
D = Customer(d.id)
E = Customer(e.id)
F = Customer(f.id)
G = Customer(g.id)




