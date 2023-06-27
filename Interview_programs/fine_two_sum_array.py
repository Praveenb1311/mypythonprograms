#Program to find out the sum of arrays

# arr = [5,7,4,3,9,8,19,21]
#sum = 17

def two_sum(arr,sum):
    arr.sort()
    left = 0
    right = len(arr)-1 # last number of array  # divide and concur
    while (left<=right):
        if (arr[left] + arr[right]>sum):
            right = right-1
        elif (arr[left] + arr[right]<sum):
            left = left+1
        else:  # we can use elif (arr[left] + arr[right]==sum): # When we mention condition use elif, if we use else no condition.
            print("Values of pair", arr[left], "and", arr[right],"sum is: ", sum)
            right = right-1
            left = left +1

arr = [5,7,4,3,9,8,19,21]
sum = 17
two_sum(arr,sum)


#2nd method:


list1 = [5,7,4,3,9,8,19,21]
n = len(list1)
m = len(list1)-1
#print(n)
#print(m)
k=17
for i in range(n):
    for j in range(i+1,n):
        if list1[i]+list1[j] == k:
            print(list1[i],list1[j])

# Method 3 Calculate by output - number is in list print all the numbers. so 8 and 9 will print

y=[3,4,5,7,8,9,19,11]
sum=17
for i in range(len(y)):
        if sum-y[i] in y:
                print(y[i])