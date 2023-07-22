list1 =[1,2,3,4,5,6]

# 1st method

# list1.reverse()
# print(list1)

# 2nd method slice

list2 = list1[::-1]
print(list2)

#3rd ,method reversed

list3 = list(reversed(list1)) # We need to type cast bcz revesed function will print
print(list3)

#4th ,method for loop

list4 = [1,2,3,4,5]
list5 = []
list6 = []
p = len(list4) -1  # len(list4)= number of elements.



# for i in range(len(list4)-1,-1,-1,):
for i in range(p,-1,-1,):  #if we use range function i will take index, if we use for in  list4 the i will count the values
# for i in range(0,len(list4),1):  #if we use range function i will take index, if we use for in  list4 the i will count the values
    list5.append(i)  #index
    list6.append(list4[i])  # index values

print("list5", list5)
print("list6",list6)


list7 = [1,2,3,4,5,5,7]

print(len(list7)-1)
print(len(list7))

