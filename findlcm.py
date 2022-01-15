import gcd

def findlcm(m,n):
    # if m>n:
    #     if m%n==0:
    #         return m
    #     else:
    #         return findlcm(m+1,n)
    #
    # else:
    #     if n%m==0:
    #         return n
    #     else:
    #         return findlcm(n+1,m)
    # lcm=(m*n)//gcd.get_gcd(m,n)
    # return lcm
    if m>n:
        greater=m
    else:
        greater=n
    while(True):
        if greater%m==0 and greater%n==0:
            return greater
        else:
            greater=greater+1




print(findlcm(3,5))
print(findlcm(8,6))
print(findlcm(10,6))