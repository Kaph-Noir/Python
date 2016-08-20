import random

sum_list = list((lambda x, y: x + y)(random.randint(1, 6), random.randint(1, 6)) for i in range(0, 1000000))

map(lambda i: print(i, ":{0:.2%} ".format(sum_list.count(i)/1000000, sep=',')), range(2, 13))
list(map(lambda i: print(i, ":{0:.2%} ".format(sum_list.count(i)/1000000, sep=',')), range(2, 13)))