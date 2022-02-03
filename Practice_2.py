list1 = [1,2,3,4,5,6,7,8,9,10,12,13,14,16,17,18,19,20]

list2 = range (1 , 21)
print(set(list2)-set(list1))

status = {"huli": "online", "praveen" : "online", "chandru" : "offline", "mabulli": "offline"}
counter = 0
name_list = []
for key, value in status.items(): #dict.items
    if value == "online":
        counter += 1
        name_list.append(key)
print(counter,name_list)

counter = 0
name_list = []
for key in status.keys(): #dict.items
        name_list.append(key)
print(name_list)

for value in status.values(): #dict.items
    if value == "online":
        counter += 1
print(counter)

status = {"huli": 32, "praveen" : 29, "chandru" : 30, "mabulli": 31}
# status = sorted(status.items(), key=lambda x:x[1])
status = sorted(status.items(), key=lambda x:x[0])
print(status)


#simple interes
