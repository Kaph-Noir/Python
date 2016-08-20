# Better Way #7

chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
# print(chile_ranks.items())

# name = ['ghost', 'habanero', 'cayenne']
# rank = [1,2,3]
rank_dict = {rank: name for name, rank in chile_ranks.items()}

print(chile_ranks)
print(rank_dict)


keys = ['a','b','c']
values = [1,2,3]
dictionary = dict(zip(keys, values))
print(dictionary)