


def employee_details(name, age, salary):
    if age >= 25:
        salary *= 1.10
    # return name,age,round(salary,2)
    return name,age,int(salary)
print(employee_details("praveen", 25, 35000))
print(employee_details("huli", 29, 4500000))
print(employee_details("mabuli", 20, 15000))
print(employee_details("ravi", 18, 5000))
print(employee_details("chandru", 35, 53000))

num1 = 2
num2 = 3
num3 = 5
#
# if num1 > num2 and num1 > num3:
#     print("largest number is ", num1)
# elif num2 > num1 and num2 > num3:
#     print("largest number is ", num2)
# else:
#     print("largest number is ", num3)

if num1 > num2 and num1 > num3:
    print("largest number is ", num1)
else:
    if num2 > num1 and num2 > num3:
        print("largest number is ", num2)
    else:
        print("largest number is ", num3)
x = 123456
y = 245678
# x,y = y,x
temp = 0
x = temp
x = y
y = x
print("x = ", x, "\ny = ",y)

d = 11

print(bin(d))
print(oct(d))
print(hex(d))

print(chr(65))
print(ord("D"))
print(ord("D")+1)

print(0b0011)
print(0x11)
print(0o11)

