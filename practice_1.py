l1 = [[0]*3]*3
l2 = [
    ["A1","B1","C1"],
    ["A2","B2","C2"],
    ["A3","B3","C3"]
]
# d = {"A":1, "B":2, "C":3}
# print(l1)
# choice = input("Please enter the value : ")
# print(int(choice[1]), d[choice[0]])

# d = {"A":0, "B":1, "C":2}
# print(l1)
# choice = input("Please enter the value : ")
# print(d[choice[0]],int(choice[1])-1)

#consegutive zero
v1 ="1000101010000001000000000"
count=0
zero_count = []
for i in range(len(v1)):
    if int(v1[i])==0:
        count += 1
    else:
        if count > 0:
            zero_count.append(count)
            count = 0
zero_count.append(count)
print(zero_count)
print(max(zero_count))
print(v1.find("0"*max(zero_count))+1)

# anagram

str1 = "lismen"
str2 = "silent"

import collections

str1_count = collections.Counter(str1)
str2_count = collections.Counter(str2)
if str1_count == str2_count:
    print("yes!!! {} and {} is a Anagram".format(str1,str2))
else:
    print("no... {} and {} is not a Anagram".format(str1, str2))

print(str1_count)
print(str2_count)

d1 = {}
for char in str1:
    if char in d1:
        d1[char] += 1
    else:
        d1[char] = 1
print(d1)


d2 = {}
for char in str2:
    if char in d2:
        d2[char] += 1
    else:
        d2[char] = 1
print(d2)
if d1 == d2:
    print("yes!!! {} and {} is a Anagram".format(str1,str2))
else:
    print("no... {} and {} is not a Anagram".format(str1, str2))



