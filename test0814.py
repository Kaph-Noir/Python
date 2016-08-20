# the green book ~p.207

square = [y**2 for y in range(10)]
print (square)

color_set1 = ['red', 'blue', 'yellow']
color_set2 = ['green', 'red', 'gray']

'''
color_scheme = []
for c1 in color_set1:
    for c2 in color_set2:
        if c1 != c2:
            color_scheme.append((c1, c2))
'''
color_scheme = [(c1, c2) for c1 in color_set1 for c2 in color_set2 if c1 != c2]

print (color_scheme)
print (len(color_scheme))