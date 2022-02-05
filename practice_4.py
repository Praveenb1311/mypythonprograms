a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
#
# c= [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(b))]# list comprension to define in for loop(inner loop first execute here)(other typical approach or normal procedure, 1first loop will be executed last
# # for item in c:
# #     print(item)
# print(c)

result = [list(map(sum, zip(*t))) for t in zip(a,b)]
print(result)
print(list(zip(a,b)))
term = list(zip(a,b))
for t in term:
    print(list(zip(*t)))
    print(list(map(sum, zip(*t))))


# list1 = range(1,10)
# list2 = range(11,20)
# print(list(list1))
# print(list(list2))
# # print(list(zip(list1, list2)))# from sequence manner its adding
# print(list(map(sum,zip(list1, list2))))
#
# list3 = range(1,5)
# list4 = range(11,20)
# print(list(list3))
# print(list(list4))
# print(list(zip(list3, list4)))
# print(dict(zip(list3, list4)))



