# 11) Дано два кортежі A i B. Перевірити, чи один з них
# входить в інший. Якщо так, то створити кортеж,
# якій містить індекс, починаючи з якого один кортеж
# входить в інший та кортеж, що входить до іншого кортежу.

from random import randint

A = tuple([randint(1,5) for x in range (20)])
B = tuple([randint(1,3) for x in range (2)])
result=[]

for E1 in range(len(A)-len(B)):
    if A[E1:E1+len(B)] == B:
        result.append(E1)
        result.append(B)
        break

print ('A:', A)
print ('B: ', B)
print(tuple(result))
