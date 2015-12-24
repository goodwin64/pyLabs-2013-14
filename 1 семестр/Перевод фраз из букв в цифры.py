abc='abcdefghijklmnopqrstuvwxyz'
ls=''
x=0
fr=input('enter your frase: ')
print ('length of your frase: ', len(fr))
while x<len(fr):
    NomerBukvy=abc.find(fr[x])
    if NomerBukvy==-1:
        print('     ')
        ls+='   '
    else:
        print(fr[x],'(',str(NomerBukvy),')')
        ls+=str(NomerBukvy)+' '
    x+=1

print (' ')
print (fr, '-', ls)
