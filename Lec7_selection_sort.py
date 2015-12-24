def selection_sort(list):
    for index in range(0, len(list)):
        iSmall = index
        for i in range(index,len(list)):
            if list[iSmall] > list[i]:
                iSmall = i
        list[index], list[iSmall] = list[iSmall], list[index] 