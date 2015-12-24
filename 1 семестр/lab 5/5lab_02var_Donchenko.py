# 2) Вивести всі парні (окремо непарні) числа, які діляться на 3 від N до M.
# Значення N та M задаються з клавіатури.

ls_parni=''
ls_neparni=''
n_str=input('Введіть число N - ліву границю: ')
m_str=input('Введіть число М - праву границю: ')
while n_str=='': # чтоб не было пустой строки
    n_str=input('Введіть число N - ліву границю: ')
while m_str=='':
    m_str=input('Введіть число М - праву границю: ')
n_float=float(n_str)
m_float=float(m_str)
n=int(n_float)
m=int(m_float)
for k in range (n, m+1):
    if k%2==0 and k%3==0:
        ls_parni+=str(k)+', '
for j in range (n, m+1):
    if (j+1)%2==0 and j%3==0:
        ls_neparni+=str(j)+', '
        
if len(ls_parni)==0:
    print('парних чисел, які діляться на 3 від', n_str, 'до', m_str, 'нема')
if len(ls_neparni)==0:
    print('непарних чисел, які діляться на 3 від', n_str, 'до', m_str, 'нема')
    
if len(ls_parni)!=0:
    print ('парні числа, які діляться на 3 від', n_str, 'до', m_str, ':')
    print (ls_parni)
if len(ls_neparni)!=0:
    print ('непарні числа, які діляться на 3 від', n_str, 'до', m_str, ':')
    print (ls_neparni)
