l1 = ["Hello","suri", "Man"]
print(len(l1))

for i in l1:   # its a wrong it is repeated 3 times
    print(l1)

for j in range(len(l1)):   # it also repeated
    print("hi",l1)

t1 = ("hi", 2, "ri", 45)
l2 = list(t1)
print(l2)
print((type))
print(l1[1])  # print 2nd value indice start from 0
print(l1[-1])
print(l1[1:])
print(l1[0:2])   # search start from indices(0) included and 2  is not included

if "hi" in t1:
    print("Yes, the word is present in list")

if "hir" not in t1:
    print("No, the word is not present in list")


l3 = ["Hello", "Hi", "How", "are", "You"]
l3[1] ="praveen"   # list is mutable and we can change the values
print(l3)

l3.insert(2, "shiva")
print(l3)

l3.append("ajja")
print(l3)
l3.extend(l2)
print(l3)

l3.remove("You")
print(l3)

# it removes the mentioned word and pop method removes the last item

l3.pop()
print(l3)

l3.pop(1)   # it removes the specified indice value
print(l3)

# del method removes the specified indices and also delete complete list

del l3[2]
print(l3)

del l3
# print(l3) NameError: name 'l3' is not defined. Did you mean: 'l1'?

#l3 list is already deleted

# del method completely delete the list

# clear metho clear the list

l4 = [34, 45, "hI", "Pr", "Sri"]
l4.clear()
print(l4)

import math
print(math.ceil(1.4))
print(math.ceil(5.3))
print(math.ceil(-5.3))
print(math.ceil(2.3))