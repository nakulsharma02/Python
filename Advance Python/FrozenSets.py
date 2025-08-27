# frozen sets are the sets which can't change their content in the set
a = [1,2,1,3,4,5,2]
frozenset1 = frozenset(a)
print(frozenset1)
'They cannot perform these Operations like frozenset.add(6)'
'They can perform operations like Union, Intersection, Subtractions and can use conditional operations like greater than or less than'
frozenset2 = frozenset([23,7,23,5,78,6])
print(frozenset1 & frozenset2)
print(frozenset1|frozenset2)
print(frozenset1 - frozenset2)
print(frozenset1>frozenset2)
for i in frozenset1:
    print(i)
print(1 in frozenset1)
print(50 in frozenset2)