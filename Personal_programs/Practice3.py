#Shifting 0 to end of the side side
list1 = [1,0,2,4,0,4,0,5,6,0,8]

for item in list1:
    if item == 0:
        list1.remove(item)
        list1.append(item)

print(list1)

#print the numbers below 100: Multiples of 2

x = 1
while x<100:
    x *= 2
print(x)

# print the numbers in list and and multiply

numbers = [2,3,4,5,6,7,8]
b =[]
for i in numbers:
    b.append(i**2)
    print(b)  # print in a pyramid format
print(b)  # print in a one line

## Nested Loop

l1 = [1,2,3,4,5,6]
l2 = [2,4,6,8]
for x in l1:
    for y in l2:
        print(x,y, sep = ".", end =",")  # seperate betweeen x and y and end = , means after one iteration


message = 'It\'s also a valid string'
print(message)

messag1 = r'C:\python\bin'
print(messag1)



