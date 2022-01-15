import gcd
def find_numberofchocolote(m,n):
    if n%m==0:
        return 1
    else:
        return m//gcd.get_gcd(m,n)


print(find_numberofchocolote(8,3))
print(find_numberofchocolote(20,5))
print(find_numberofchocolote(24,8))
print(find_numberofchocolote(6,5))
print(find_numberofchocolote(16,10))
print(find_numberofchocolote(17,5))
print(find_numberofchocolote(4,8))
