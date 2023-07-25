class Car:

#Class has a attributes and behaviour

# Namespace : is the area where you are going to create and store object/variable
#2 types of namespace where you will store all the class namespace and object/instance name space

	Wheel = 4   # class variables if we ned to change this we need to change with class

	def __init__(self):
		self.mil = 10     # static variables so it can change as per below
		self.com = "BMW"

c1 = Car()
c2 = Car()

print(c1.com, c1.mil)
print(c2.com, c2.mil)

c1.mil = 9   # we are changing the variables

print(c1.com, c1.mil)



print(c1.com, c1.mil, c1.Wheel)
print(c2.com, c2.mil, c2.Wheel)


Car.Wheel = 5 # it will change all the wheel values.


print(c1.com, c1.mil, c1.Wheel)
print(c2.com, c2.mil, c2.Wheel)


# Methods: Class methos, instance method and static method

class stud:
	school = "ssvhs"
	def __init__(self,m1,m2,m3):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3

	def avg(self):
		return (self.m1 + self.m2 + self.m3) / 3

	def get_m(self):
		return "hello"
		pass

	def set_m(self):  # insted of defining one variable we can define set and get
		return "hi"
		pass


	@classmethod     # decorator
	def info(cls):
		return cls.school

s1 = stud(13, 14, 15)
s2 = stud(33, 34, 35)

print(s1.avg())
print(stud.info())   #to avoid some error add constructor

