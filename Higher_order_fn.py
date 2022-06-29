#map reduce filter
def square(x):
    return x*x

l1 = [ 1, 2 , 3, 4, 5]

squared_list = tuple(map(square,l1))

print(squared_list)

squared_list = list(map(lambda x:x*x,l1)) #annonymous(there is no name) function  (int 2power 15)
print(squared_list)
print(squared_list)
square = lambda y:y**10
print(square(2))