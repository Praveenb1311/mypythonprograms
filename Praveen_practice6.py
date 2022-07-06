maha = "holiday"
# sorted_list = sorted(maha)
reversed_list = 0
print(maha[::-1])

num1 = "HARFJ"
num2 = "harish"
print(num1.lower())
print(num2.upper())
print(num2.replace("harish","praveen"))

# print("".join(sorted(maha)))
import random
die1 = random.randint(1,6)
die2 = random.randrange(6)
print(die1)
print(die2)

# # mood = random.randint(1,3)
# mood = int(input("enter any numbers from 1 to 3 : "))
# if mood == 1:
#     print("you are very very happy")
# elif mood == 2:
#     print("you are neutral")
# else:
#     print("you are so sad")

a = 10
b = 3
# print(max(a,b))
# if a >= b:
#     print(a)
# else:
#     print(b)
max = int(lambda a,b:a if a > b else b)
print(max)
