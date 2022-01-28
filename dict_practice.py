# # list = [1,2,3,4,5]
# list = {1,2,3,4,5}
# # list = (1,2,3,4,5)
#
# list.clear()
#
# print(list)


# marks = {'physics' :67, 'Chemistry' :58, 'maths' : 99}
# internal_marks = {'practical' :28}
#
# marks.update(internal_marks)
#
# print(marks)

# d = {1:'one', 2: 'three'}
# d1 = {2:'two'}
#
# d.update(d1)
# print(d)
# d[2] = "huli"
#
# d1 = {3: 'three'}
#
# d.update(d1)
# print(d)

#
# d = {'x' :2}
# d.update(y=3,  z=4) #to represent dict in touple
#
# print(d)
#
# # vowels keys
# keys = {'a', 'e', 'i', 'o', 'u' }
# value = [1]
#
# vowels = { key : list(value) for key in keys }
# # you can also use { key : value[:] for key in keys }
# print(vowels)
#
# # updating the value
# value.append(2)
# print(vowels)

# d = {1:'one', 5: 'five', 4: 'four', 2: 'three'}
#
# print(d)
#
# d = sorted(d.items(), key=lambda x:x[1])
#
# print(dict(d))
#
# add = lambda a,b: a+b
# print(add(5,6))
#
# def add(a,b):
#     return a+b
# print(add(5,6))
#
# list1 = [1,'shs', 2,3,4,5]
#
# list1.remove('shs')
#
# print(list1)
#
# int a # object
#
# #Set

list1 = [1,'shs',5,3,2,3,4,5]

set_A = set(list1)

print(set_A)

set_B = {1,2,4,3}

print(set_A-set_B)
print(set_B-set_A)
print(set_B.issubset(set_A))
print(set_A.issuperset(set_B))
print(set_A.intersection(set_B))
print(set_A.union(set_B))
print(set_B.union(set_A))