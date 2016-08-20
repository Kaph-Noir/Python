import random

# sum_lis = [i for i in range(10)]
sum_list_test = [(lambda x,y: x+y)(random.randint(1,6), random.randint(1,6)) for i in range(1000000)]

# print(sum_lis_test)
# sum_list = list((lambda x, y: x + y)(random.randint(1, 6), random.randint(1, 6)) for i in range(0, 100))

map(lambda i: print(i, ":{0:.2%} ".format(sum_list_test.count(i)/1000000, sep=',')), range(2, 13))
list(map(lambda i: print(i, ":{0:.2%} ".format(sum_list_test.count(i)/1000000, sep=',')), range(2, 13)))