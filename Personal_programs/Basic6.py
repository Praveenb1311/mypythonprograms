# class student:
#     def __init__(self, name):
#         self.name = name
#
#
#
# st = student("rahul")
# print(st)

class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("The values of cpu and ram are", self.cpu, self.ram)


cnf1 = Computer("i5", 17)
cnf2 = Computer("Rayen 3", 17)

cnf1.config()
cnf2.config()



class Student:

    def __init__(self):
        self.name = "Pravin"
        self.age = 30
    def update(self):
        self.name = "raki"

c1 = Student()
c2 = Student()

c1.name = "rashi"
c1.age = 30



print(c1.name)
print(c2.name)

c1.update()

print(c1.name)

