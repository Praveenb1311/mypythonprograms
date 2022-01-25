number1 = "123"
number2 = "876"

# sum = int(number1) + int(number2)
sum = eval(number1) + eval(number2)  # evaluate

print(sum)

str1 = "alphabet"
str1 = "crunchi"
str1 = "madam"

import collections

countdict = collections.Counter(str1)

for index, letter in enumerate(str1):
    if countdict[letter] == 1:
        print(index+1,letter)
        break
# print(countdict)

list1 = [1,5,9,1,8,9,4,5]
list1 = [1,2,3,4,5]
list1 = [8,5,2,1]

def find_monotonic(list1):
    return (
        all(list1[i] >= list1[i+1] for i in range(len(list1)-1)) # all will be used only for all true
        or
        all(list1[i] <= list1[i+1] for i in range(len(list1)-1))
    )
print(find_monotonic(list1))

list1 = [8,5,2,1]
# list1 = [1,2,3,4,5]

# list1 = [1,5,9,1,8,9,4,5]


for i in range(i+1, len(list1)):
    if i >= j:
        flag = False
     else:
            flag = True


    # for j in range(i+1,len(list1)):
    #     if j <= i:
    #         flag1 = True
    #     else:
    #         flag1 = False

print(flag)
