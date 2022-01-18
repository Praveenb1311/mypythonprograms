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

def cubing_number(n):
    for i in range(1,n+1):
        print("{} x {} x {} = {}".format(i,i,i,i*i*i))

cubing_number(25)