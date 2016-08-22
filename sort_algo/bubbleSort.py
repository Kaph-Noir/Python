# by myself
def bubbleSort(lst):
    for i in range(1,len(lst)):
        # print(i)
        j = i-1
        while lst[j] > lst[j+1] and j >= 0:
            # print(j)
            lst[j+1], lst[j] = lst[j], lst[j+1]
            # tmp = lst[j+1]
            # lst[j+1] = lst[j]
            # lst[j] = tmp
            j -= 1
            print(i)
            print(lst)
    return lst

def bubbleSort1(lst):
    for i in range(len(lst)-1, 0, -1):
        j = i-1
        # print(i)
        print(j)
        while lst[j] > lst[j+1] and j >= 0:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            # tmp = lst[j+1]
            # lst[j+1] = lst[j]
            # lst[j] = tmp
            j -= 1
            print(lst)
    # return lst

# by prof.Kim
def bubble_sort(a_list):
    for pass_num in range(len(a_list)-1,0,-1):
        for i in range(pass_num):
            if a_list[i] > a_list[i+1]:
                temp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = temp
    return a_list

# from wikipedia
def wk_bubbleSort(x):
    length = len(x) - 1
    # print(length)
    for i in range(length):
        # print(i) 0 1 2 ...
        for j in range(length - i):
            if x[j] > x[j+1]:
                x[j], x[j + 1] = x[j+1], x[j]
    return x

# i = [7,6,5,4,3,13,15,12,31,24,36,67,2]
# print(len(i))
# p = bubbleSort(i)
# print(p)

i = [7,6,5,4,3,13,15,12,31,24,36,67,2]
print(i)
p = bubbleSort1(i)
# print(p)
'''
i = [7,6,5,4,3,13,15,12,31,24,36,67,2]
p = bubble_sort1(i)
print(p)

i = [7,6,5,4,3,13,15,12,31,24,36,67,2]
p = wk_bubbleSort(i)
print(p)
'''