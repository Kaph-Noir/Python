numbers = 'A23456789TJQK'
marks = 'SDHC'
cards = [n+m for m in marks for n in numbers]
ranks = [i+1 for i in range(10)]
for i in range(3):
    ranks.append(10)

for i in range(3):
    ranks += ranks

# print(ranks)
# print(type(ranks))
print(cards)

score = {}
for key in range(len(cards)):
    print(cards[key])
    print(ranks[key])
    score[cards[key]] = ranks[key]

# print(type(score))
print(score)
