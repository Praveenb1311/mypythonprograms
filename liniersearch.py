key=70
test_list = [2,5,10,30,50,70]
flag=False
for i in range(len(test_list)):
    if test_list[i]==key:
        print("element found at ", i+1)#this is natural way of print(Programing way of print start from 0)
        flag=True
        break

if flag==False:
    print("element not found")
