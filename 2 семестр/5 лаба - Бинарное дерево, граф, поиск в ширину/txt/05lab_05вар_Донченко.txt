# 5. Соціальну мережу можна представити у вигляді орієнтованого графа,
# де вершинами є облікові записи користувачів. Використовуючи пошук
# в ширину знайдіть спільних друзів, та спільних друзів друзів двох
# користувачів. Виведіть їх список.

from random import randint

NameList = ['Ваня', 'Макс', 'Стёпа', 'Игорь', 'Жека', 'Серега', 'Веталь', 'Андрюха', 'Саня']
SurnameList = ['Стасюк', 'Донченко', 'Конюхов', 'Лавровский', 'Шпак', "Сериков"]
idList = [x for x in range(1, 1001)] # 1к пользователей в соц. сети
Base_of_Users = {} # База данных пользователей соц. сети





class FaceBookUser(object):
    '''Пользователь соц. сети'''

    def __init__(self, name, surname, id_number):
        self.name = name
        self.surname = surname
        self.id = id_number
        self.FriendList = []
        Base_of_Users [self.id] =  [name, surname, self.FriendList]

    def __str__(self):
        return '{0} {1}, id={2}'.format(self.name, self.surname, self.id)

    def new_friend(self, Friend):
        self.FriendList.append( (Friend.name, Friend.surname, Friend.id) )
        Friend.FriendList.append( (self.name, self.surname, self.id) )

    def mutual_friends(self, Other):
        mutual_List = []
        for E in self.FriendList:
            if E in Other.FriendList:
                mutual_List.append(E[0:2])
        return 'Общие друзья: ' + str(mutual_List)

    def friends_friends(self):
        FF_list = [] # временный список друзей друзей пользователя
        for Tuple_of_friends in Base_of_Users [self.id][2]: # кортеж каждого друга в списке друзей
            for Fr_Data in Base_of_Users [Tuple_of_friends [2]] [2]: # Данные каждого друга каждого друга
                FF_list.append(Fr_Data[2]) # в этом кортеже 3й элемент - id друга
        return set(FF_list)

    def mutual_friends_friends(self, Other):
        mutual_List = []
        for E in self.friends_friends():
            if E in Other.friends_friends():
                mutual_List.append(Base_of_Users[E][0:2])
        return 'Общие друзья друзей: ' + str(mutual_List)



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
b.new_friend(c)
b.new_friend(e)
d.new_friend(c)
c.new_friend(f)
# "b" и "c" - не друзья
# У пользователя А: друзей 2 (B, C), друзей друзей 4 (A, D, E, F)






