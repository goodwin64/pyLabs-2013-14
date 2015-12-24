import random
def list_gen(n):                                 ##Генерация списка автоматически
    A=[]
    for i in range(n):
        A.append(int(random.random()*100))
    return A
#____________________________________________________________________
def list_input(n):                                #Генерация вводом поэлементно
    A=[]
    for i in range(n):
        A.append(int(input("Введите элемент №"+str(i)+" :")))
    return A
#____________________________________________________________________
def bubble_sort(A,B):                           #Пузырьковая сортировка              
    A.extend(B)
    c=True
    while c:
        c=False
        for i in range(len(A)-1):
            if A[i]>A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
                c=True
    return A               
#_____________________________________________________________________
                                                  #Сортировка вставкой
def insertion_sort(A,B):
    A.extend(B)
    for i in range(1,len(A)):
        j=i-1
        key=A[i]
        while (A[j]>key) and j>=0:
            A[j+1]=A[j]
            j-=1
        A[j+1]=key
    return A    
#______________________________________________________________________
                                                   #Сортировка выбором
def selection_sort(A,B):
    A.extend(B)
    for index in range(len(A)):
        s=index
        for i in range(index,len(A)):
            if A[s]>A[i]:
                s=i
        A[index],A[s]=A[s],A[index]
    return A   
        
                
    

    
