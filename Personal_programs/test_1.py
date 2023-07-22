
a = 27
b = 30
sum = a+b
print(sum)

list

print(f"{a} year old", end = ": ")
print("{} year old".format(a))
print("sum of {} and {} is {}".format(a, b, sum))

# round of operations


# %d, %s, %f, /n, end ="",
#
# x = 5.42364
#
# print(x%.2f)

import itertools
numbers = [1, 2, 3]
result = list(itertools.permutations(numbers))


# def myFun(arg1, argv):
#     print("First argument :", arg1)
#     # for arg in argv:
#     #     print("Next argument through *argv :", arg)
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


def myFun(**kwargs):
    print("This are keys and values")
    for key, value in kwargs.items():
        print("{} == {}".format(key, value))


    print("This are keys")


    for key in kwargs.keys():
        print("{}".format(key))


    print("This are Values")


    for value in kwargs.values():
        print("{}".format(value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')