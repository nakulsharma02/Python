# a={1,3,5,7}#sets are mutable
# print(a,type(a))
# b=set([3,2,1])
# print(b,type(b))
'''Unordered: Sets do not maintain the order of elements.
Unique Elements: Duplicate elements are not allowed.
Mutable: You can add or remove elements after creation.
No Indexing: Sets do not support indexing, slicing, or other sequence-like behavior.'''
#set methods
# abc={3,7,8,2,9,0}
# abc.add(78)#to add element in the last 
# print(abc,type(abc))
# alice=abc.copy()#copy method
# print(alice,type(alice))
# abc.discard(2)#removes an element from the set if it is present. Does nothing if the element is not present
# print(abc)
# abc.update({3,4,5,6,20})#update the set
# print(abc)
# abc.pop()#takes no argument delete the first element
# print(abc)
# abc.remove(4)#give the key error if element is not present
# print(abc)

#set functions
# print(len({1, 2, 3}))
# print(sorted({3, 1, 2}))
# print(any({0,1,2,3}))#gives true if non zero values are present
# print(all({1,2,3}))#give true if all elements are non zero
# print(sum({1,2,3,4,5,6,7,8,9,10}))

#set operations
# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# print(s1.union(s2), s1.intersection(s2),s1.difference(s2), s1.symmetric_difference(s2),s1.issubset(s2),s1.issuperset(s2),s1.isdisjoint(s2))
