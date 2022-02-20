# Python Program to find the area of triangle

a = 5
b = 6
c = 7

# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is : {:.2f}'.format(area))

# Area of circle
PI = 3.1416
r = 7
area = PI * r * r
print('The area of the circle is : {:.2f}'.format(area))

# Area of rectangle

a = 5
b = 6

area = a * b
print('The area of the rectangle is : {:.2f}'.format(area))


# Area of cylinder

PI = 3.1416
r = 7
h = 8
area1 = 2* PI * r * r
area2 = 2* PI * r * h
area = area1 + area2
print('The area of the cylinder is : {:.2f}'.format(area))


# square

print(2 ** 10)



