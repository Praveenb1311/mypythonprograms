import copy

a = 5
b = a
print(a,b)
b = 6
print(a)
a = 7
print(b)
print(a,b)

l1 = [1,2,3,4,5]
l2 = [4,5,6,7]

l1 = copy.deepcopy(l2)
print(l1)


l1 = [1,5,6,4,5]
l2 = [4,5,6,7]

l1 = copy.copy(l2)
print(l1)
