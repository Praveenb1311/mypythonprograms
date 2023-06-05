year = int(input("Please enter the Year: "))
if (year % 4 == 0) and (year % 100 !=0):
    print("Given year is a Leap Year")
elif (year % 400 == 0) and (year % 100 ==0):
    print("Given year is a Leap Year")
else:
    print("Given year is not a Leap year")





