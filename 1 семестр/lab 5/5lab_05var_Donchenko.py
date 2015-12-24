# 5) Дано натуральне число N. Серед чисел 1, ..., N
# знайти такі числа, запис яких співпадає з останніми
# цифрами запису їх квадрату.

while True:
    Granytsja=int(input('n: '))
    for DoslydneChyslo in range (1, Granytsja+1):
        KilkistCifr=0
        n=int(DoslydneChyslo)
        while n>0:
            n=int(n/10)
            KilkistCifr+=1
        D2=DoslydneChyslo**2 # квадрат дослідного числа
        if str(DoslydneChyslo)==str(D2)[-KilkistCifr:]:
            print (DoslydneChyslo, '^ 2 =', D2)
    print('')
    Active=input('Продолжать? в случае отказа введите "нет"   ')
    print('')
    if Active=='нет':
        break
