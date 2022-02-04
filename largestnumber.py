# def largest_number(list1):
#     big = list1[0]
#     for item in list1[1:]:
#         if item > big:
#             big=item
#     return big
# 
# print(largest_number([1,2,3,4,5,6]))
# print(largest_number([8,2,3,4,5,6]))
# 
# def smallest_number(list1):
#     small = list1[0]
#     for item in list1[1:]:
#         if item < small:
#             small=item
#     return small
#
# print(smallest_number([1,2,3,4,5,6]))
# print(smallest_number([8,2,3,4,5,6]))
# print(min([8,2,3,4,5,6]))
# print(max([8,2,3,4,5,6]))

# def multiplication_factor(n):
#     for i in range(1,11):
#         print("{} x {} = {}".format(n,i,n*i))
#
# multiplication_factor(5)
# multiplication_factor(12)
# multiplication_factor(3)

#
# def squring_number():
#     for i in range(1,11):
#         print("{} x {} = {}".format(i,i,i*i))
#
# squring_number()

# def squring_number(n):
#     for i in range(1,n+1):
#         print("{} x {} = {}".format(i,i,i*i))
#
# squring_number(25)

# def cubing_number(n):
#     for i in range(1,n+1):
#         print("{} x {} x {} = {}".format(i,i,i,i*i*i))
#
# cubing_number(25)

# def round_off(n,decimalplaces):
#     return round(n,decimalplaces)
# print(round_off(5.6875,2))
# print(round_off(3.3456,3))
# print(round_off(5.6875,4))
# print(round_off(5.6875,1))
# print(round_off(5.6875,0))

list1 = [25.6356356,25.635634,25.345,25.3467,25.3489,25.6389]

round_off_list = [round(i,2) for i in list1]
print(round_off_list)

# dict = {}
# for item in round_off_list:
#     if item in dict:
#         dict[item] += 1
#     else:
#         dict[item] = 1
#     # print(dict)
# print(dict)
#
# import collections
# output = collections.Counter(round_off_list)
# print(output)

# print(output.most_common(1))
# print(output.most_common(2))

dict = {}
for item in round_off_list:
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1
    # print(dict)
print(dict)

values = list(dict.values())

max_value = max(values)

for key,value in dict.items():
    if max_value == value:
        print(key,":", value)
        break


a = 25.999999
b = 25.0001
# a = float(input("enter the value of a : "))
# b = float(input("enter the value of b : "))
import math

print("floring value of {} = {} ".format(a, math.floor(a)))
print("ceiling value of {} = {} ".format(b, math.ceil(b)))
# print(math.ceil(b))

