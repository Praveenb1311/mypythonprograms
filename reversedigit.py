# n=12345
# Reverse=0
# while n>0:
#     Rem=n%10
#     Reverse=Reverse*10+Rem
#     print("n", n, "n%10", n % 10, "Reverse", Reverse)
#     n=n//10
#
# print(Reverse)

# for loop
n=12345
Reverse=0

for i in range(1,len(str(n))+1): #for loop end before a step
    print("step",i)
    Rem=n%10
    Reverse=Reverse*10+Rem
    print("n", n, "n%10", n % 10, "Reverse", Reverse)
    n=n//10

print(Reverse)
