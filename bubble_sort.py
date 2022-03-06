list1 = [12,5,8,6,10]
#step1_ 2>5, 2>8, [2,5,8,6,10]
# step2 5 to 8, [2,5,8,6,10]
# step 3 8 is not < 6 replace [2,5,6,8,10]
# step 4 10
# list1.sort()
# print(list1)

for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] > list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp
print(list1)

