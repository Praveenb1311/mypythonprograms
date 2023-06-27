import random
food = ["pizza", "Fruits", "Chiroti"]
dinner = random.choice(food)
print(dinner)

print("Random number is: ", random.randint(0,5))  # Randint generates the numbers from 0 to 5


list1 = [1,2,3,4,5,8,6,7,8]
print(max(set(list1)))#, key = list1.count)
x = set(list1)#, key = list1.count)
print(type(x))
print(set(list1))#, key = list1.count)
print(max(set(list1), key = list1.count))#, key = list1.count)

print(sum(i for i in range(5)))  # A dding each element or counting the all numbers


# Program to check for anagrams: which means all the characters should be same.

x = "Listen"
y = "Silent"

p = sorted(x.lower())
q = sorted(y.lower())

print(p)
print(q)

if p == q:
    print("Given names {} and {} are anagram.".format(x,y))
else:
    print("Given names {} and {} are not anagram.".format(x,y))


name = "Hello how are you?"
# sp = name.split()
# print(sp)
# for i in sp:
#     print(i, end =",")


# word1 = name.split()
word1 = name.split(maxsplit=1)
import time  # making the time delay
time.sleep(5)
word2 = name.split(maxsplit=2)
print(word1)
print(word2)



print(len(word1))




for i in word1:
         print(i, end =",")