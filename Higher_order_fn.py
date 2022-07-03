#map reduce filter
# def square(x):
#     return x*x
#
# l1 = [ 1, 2 , 3, 4, 5]
#
# squared_list = tuple(map(square,l1))
#
# print(squared_list)
#
# squared_list = list(map(lambda x:x*x,l1)) #annonymous(there is no name) function  (int 2power 15)
# print(squared_list)
# print(squared_list)
# square = lambda y:y**10
# print(square(2))


#import functools
from functools import reduce
list1 = [1,3,5,6,2]
l1 = range(1,10)

print("the sum of list1 elements: ", end = "")
print(reduce(lambda a, b: a+b, list1))   # function for the sum of element

print("the sum of l1 elements: ", end = "")
print(reduce(lambda a, b: a+b, l1))


print("the maximum element of the list1 is: ", end = "")
print(reduce(lambda a, b: a if a > b else b, list1))   # function for maximum number

print("the maximum element of the l1 is: ", end = "")
print(reduce(lambda a, b: a if a > b else b, l1))

list2 = [0, 1, 2, 3, 5, 8, 13]

result = filter(lambda x: x % 2 != 0, list2) #indentation: (iterator object)
print("odd numbers of the list2 : ", list(result))

result = filter(lambda x: x % 2 == 0, list2)
# print("even numbers of the list2 : ", list(result))
# print(list(result))

# print("even numbers of the list2 : ", print(list(result)))
# hello = print("huli")

# print(hello)

def print1(s):print(s)
    # return s
print(print1("hello"))