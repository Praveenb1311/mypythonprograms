import numpy as np

x = np.full((4, 5),4)
print(x)
print(x[0,2])
x[0,2] = 5
print(x)

#since the list is integer w=if we provide float value also it takes int value

x[0,1] = 3.14 # which assigns only 3
print(x)

y = np.random.randint(3,10)
z = np.random.randint(10, size=6)
p = np.random.randint(10, size=(2,3))  # it creates rows and column
print(y)
print(z)
print(z[0:2]) # it operates similRLY TO SLICE
print(z[:2]) # it is also same a sabove
print(z[-1]) # last
print(z[0::3]) # step
print(z[::-1]) # reverse
print(p) #

a = [1,2,3,4]
b = [5,6,7,8]
print(np.concatenate[a,b])
#vstack and hstack are used for multidimentional array
print(np.vstack[y,p])
print(np.hstack[y,p])
output = np.empty(len(10))
print(output)




