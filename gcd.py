def get_gcd(m,n):
    print("m",m, "n", n, "m%n", m%n)
    if m%n==0:
        return n

    else:
        return get_gcd(n,m%n)



print(get_gcd(2,3)) #commpile time input or static input, other types RUN TIME INPUT or DYNAMIC INPUT
# print(get_gcd(5,10))
# print(get_gcd(30,50))
# print(get_gcd(8,6))
# print(get_gcd(4,10))

print(get_gcd(20,30))

m = int(input("enter the value of m : "))
n = int(input("enter the value of n : "))
# print(get_gcd(m,n))
print("gcd of {} and {} = {}".format(m, n, get_gcd(m,n)))

