def test(x):
    i = 0
    for i in x:
        print(i)
        print(x[i])
        if x[i] > 3:
            return True
        else:
            return False
l = [0,1,10,11,100]
for j in range(5):
    key = int(input('input: '))
    l[j] = key
    print(l)
    p = test(l)

print(p)