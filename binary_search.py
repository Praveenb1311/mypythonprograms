list1 = [1,2,3,4,5,6,7,8,9] #in binary or dit it should be in sorting order
key = 10
# if key in list1:
#     print("yes!!! key found")
# for item in list1: #linear search by 9 iteration
#     if key == item:
#         print("key found")
#         break

low = 0
high = (len(list1)-1) #convering to 8 th index

while(high >= low): # check the condition before
    mid = (low + high)//2  # flooring division-//
    if list1[mid] < key:
        low = mid+1
    elif list1[mid] > key:
        high = mid - 1
    else:
        print("key {} found at {}".format(key, mid))
        break




