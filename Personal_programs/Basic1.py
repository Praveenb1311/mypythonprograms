# print i as long as i is less than 6

i = 1
while i < 6:
    print(i)
    i += 1

# Exit the loop when i = 3
x = 1
while x < 6:
    print(x)  #it prints 1,2,3
    if x == 3:
        break
    # print(x)   it prints 1,2
    x += 1


#unpacking
list1 = ["helo", "how", "are", "you?"]
p,q,r,s = list1
print(p,q,r,s)
# print(p)
# print(q)
# print(r)
# print(s)
# Global Variables.
a = "Awesome"
def myfunc():
    global a
    a = "Fentastic"
# myfunc() if we didnt call this function it takes the local variable
print("python program is a", a)

print(memoryview(bytes(5)))

import random

print(random.randrange(1,10))
print(random.randint(100000,999999))

b = "Hello"
print(b[1])
print(len(b))
for c in b:    # accessing the elements throgh loops
    print(c)

d = "Hello how are you"
print(len(d))

txt ="The best thing in our life are free!"
print("free" in txt)   # to check the word in string
if "life" in txt:
    print("the given word is in string")
if "express" not in txt:
    print("the given word is not in string")
print("genious" not in txt)

e = "Praveenmeghana"
print(e[:2])    # START FROM 0 indices 2 indice value is not included
print(e[5:])   # search start from 0 5 is not included
print(e[3:7])  # print the letter from 2 to 7(not included 3, 7) start from 0 and 3 indice is not included
print(e[-5:-2])  # - means start frpm -1 to -5 included to -2 not included
# means :digit - print the value till the last digit cont from 1
# 2: print after 2 numbers not include this letter
# but last letter includes

f = "Hello, World"
g = f.upper()
print(g)
h = f.lower()
print(h)

j = f.capitalize()  # First letter capitalized
print(j)
k = " Hello, I am not feeling well!  "# strip removes fron and last spaces
print(k.strip())
print(k.replace("H","P"))
print(k.replace("not","was"))

l = "My name is Praveen"
print(l.split())
print(l.split(","))  # it removes the , combains one string

hello1 = "Hi my name is \" John \" and I would like music"
print(hello1)      # use \ for escape sequesnce, \"

m =1        # Format string
n= 34
o =234
print("the value of {} and {} are the types of {}".format(m,n,o))


# boolian

print(4>5)
print(10>5)
print(10==5)

print(bool(5))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))

def myfunct1():
    return False
print(myfunct1())

if myfunct1():
    print("Yes")
else:
    print("No")

r = 200
print(isinstance(r, int))

str12 = "Hello I am praveen"
print(str12[1])
print(str12[1:3])  #start from start indice and end from end-1(end indice not printed

pr = "Hello sir Good morning"
#print(pr.replace("Hello","s"))  # string will not replace since its a immutable language.

# so we need to assign to new variable

pr1 = pr.replace("o","a")
print(pr1)
pr1 = pr.replace("Hello","Hi")
print(pr1)

