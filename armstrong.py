for i in range(1001):
    num = i
    result = 0
    n = len(str(i))
    while (i != 0):  # when i divides with 10 last digit was 1or upto 9 // 10 = 0
        digit = i % 10
        result = result + digit ** n
        i = i // 10

    if num == result:
        print("Armstrong numbers from the range 1 to 4 are: ", result)
