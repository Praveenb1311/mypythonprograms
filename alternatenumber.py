# test_list= [1,6,7,8,30,32,21]
#
# print("original list : "+ str(test_list)) # static string and dynamic string
# alt_list=[]#empty array
# for i in range(len(test_list)):
#
#     if i%2 != 0:
#         print(test_list[i], end= ",") #by defauslt end= /n(which means next line)
#         alt_list.append(test_list[i])#append means adding the number(if condition pass)
# print()
# print("alt_list : ", alt_list)

test_list= [1,6,7,8,30,32,21]

print("original list : "+ str(test_list)) # static string and dynamic string
alt_list=[]#empty array
for i in range(len(test_list)):

    if i%2 == 0:
        print(test_list[i], end= ",") #by defauslt end= /n(which means next line)
        alt_list.append(test_list[i])#append means adding the number(if condition pass)
# print()
print("alt_list : ", alt_list)
