# 10) Визначити, чи є задане шестизначне число
# “щасливим” (сума перших трьох цифр має
# дорівнювати сумі останніх трьох цифр)?

while True:
    first_x_str=input('Введіть шестизначне число: ')
    if first_x_str=='STOP':
        break
    while len(first_x_str)!=6:
        first_x_str=input('Введіть ШЕСТИЗНАЧНЕ число: ')
    x_str=str(first_x_str)
    
    S123=0
    S456=0
    while len(x_str)!=3:
        S456+=int(x_str[-1])
        x_str=x_str[:len(x_str)-1]
    while len(x_str)>0:
        S123+=int(x_str[-1])
        x_str=x_str[:len(x_str)-1]

    if S123==S456:
        print('Число', first_x_str, 'щасливе')
    else:
        print('Число', first_x_str, 'не є щасливим')
    
