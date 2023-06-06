a = int(input("Please enter the number: "))
if a>1:
    for x in range(2,a):
        if ((a%x) == 0):
            print("Given number is not a prime number")
        else:
            print("Given number is a prime number")
else:
    print("Not a Prime number")