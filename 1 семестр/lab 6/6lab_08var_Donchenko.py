# 8) Дано два списки. Найти їх перетин – ті елементи,
# які є в обох списках, і зберегти їх до кортежу.

from random import randint

A = [randint(1,10) for x in range (5)]
B = [randint(1,10) for x in range (5)]
result=[]

for E1 in A:
    for E2 in B:
        if E1 == E2:
            result.append(E1)

print ('A:', A)
print ('B: ', B)
print('Спільні елементи для обох списків: ', tuple(result))
