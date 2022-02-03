p = float(input("enter princple value: "))
t = float(input("enter tenure period: "))
r = float(input("enter rate of interest: "))

interest = (p * t * r) / 100
amount = interest + p
print(interest)
print(amount)


