

# n=17
#
# flag=False
# for i in range(2,n//2):
#     print(n%i, "n%i")
#     if (n%i==0):
#         flag = True
#         break
#
# if flag:
#     print(n,"is not a prime number")
#
# else:
#     print(n, "is a prime number")

import math
n=97

flag=False
for i in range(2,int(math.sqrt(n))+1):
    print(n%i, "n%i")
    if (n%i==0):
        flag = True
        break

if flag:
    print(n,"is not a prime number")

else:
    print(n, "is a prime number")