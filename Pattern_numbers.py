n = int(input("enter the number of rows: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end = "")
    print()


n = int(input("enter the number of rows: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end = "")
    print()


n = int(input("Please enter the number of rows: "))
for row in range(n):
    for col in range(n):
        if col == 0 or row == (n-1) or row == col:
            print("*", end ="")
        else:
            print(end = " ")
    print()