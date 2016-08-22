def insertSort(lst):
    for i in range(1, len(lst)):
        j = i-1
        key = lst[i]
        # print('i: ', i)
        while lst[j] > key and j >= 0:
            # print('j: ', j)
            lst[j+1] = lst[j]
            j -= 1
            lst[j+1] = key
    return lst

i = [7,6,5,4,3,2]
p = insertSort(i)
print(p)