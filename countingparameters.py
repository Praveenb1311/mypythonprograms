# def count_parameter(name,age):
#     #position based parameter-maintain the same position
#     print("my name is {} and I am {} years old".format(name,age) )
#
#
# count_parameter("praveen",29)
# count_parameter(29,"praveen")
# # position based parameter-maintain the same position
# def count_parameter(name= "praveen",age=29):
#
#     print("my name is {} and I am {} years old".format(name,age) )
#
#
# count_parameter(name="huli",age=30)
# count_parameter(name="huli")
# count_parameter(age=31)
# count_parameter(age=28,name="mabulli")
# count_parameter(29,"praveen")
# key word parameter-if we interchange position also it will not consider

# def count_parameter(*args):
#     return len(args)
#
# print(count_parameter(1))
# print(count_parameter("name",3))
# print(count_parameter(4,5,6))
# print(count_parameter())

# XOR-operation
# def xor_operation(n,l1,l2):
#     if n in l1 and n in l2:
#         return False
#     elif n in l1 and n not in l2:
#         return True
#     elif n not in l1 and n in l2:#else if is condition
#         return True
#     else: #n not in l1 and n not in l2:
#         return False

def xor_operation(n, l1, l2):
    # if n in l1 and n in l2:
    #     return False
    # elif n in l1 or n in l2:
    #     return True

    # else:
    #     return False

    return not (n in l1) ^ (n in l2) #xnor operation =overall output+ not
print(xor_operation(1,[1,2,3,4,5],[2,5,1,4]))
print(xor_operation(1,[1,2,3,4,5],[2,5,4]))
print(xor_operation(1,[3,4,5],[2,5,1,4]))
print(xor_operation(1,[2,3,4,5],[2,5,4]))
