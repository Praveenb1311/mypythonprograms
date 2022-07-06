# insertion sort:



# step1: 6 we need to keep it as constant or reference element,(1,2)
# 6,11,35,8,13,95,18
#step2: 35 we need to keep it as constant or reference element,(1,2,3)
# 6,11,35,8,13,95,18
#step3: 8 we need to keep it as constant or reference element,(1,2,3,4)
# 6,8,11,35,13,95,18
#step4: 13 we need to keep it as constant or reference element,(1,2,3,4,5)
# 6,8,11,13,35,95,18
#step5: 95 we need to keep it as constant or reference element,
# 6,8,11,13,35,95,18
#step6: 18 we need to keep it as constant or reference element,
# 6,8,11,13,18,35,95


# for i in range(len(list1)):
#     for j in range(i+1, len(list1)):
#         if list1[i] > list1[j]:
#             temp = list1[i]
#             list1[i] = list1[j]
#             list1[j] = temp
# print(list1)
#
# list1 = [11,6,35,8,13,95,18]

# for i in range(1, len(list1)):
#     k = list1[i]       # k is the ref element
#     j = i-1
#
#     while(j >= 0 and k < list1[j]):
#         list1[j+1] = list1[j]
#         j -= 1
#     list1[j+1] = k
#     print(list1)
# print(list1)
# #

# merge_sort:
# 2 sorted lists were given
list1 = [2, 4, 6, 8, 10]

list2 = [3, 5, 7, 9,11]

list3 = []

# compare the first values of each list and check which value will be greate
i = 0
j = 0
while i < (len(list1)-1) and j < (len(list2)-1):

    if list1[i] > list2[j]:
        list3.append(list2[j])
        j += 1
    else:
        list3.append(list1[i])
        i += i
    print(i,j)

print(list3)

