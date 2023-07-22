def func1():
    print("I am learning python function")

func1()

def multipy1(x,y=0):
    return x*y

x = multipy1(4, 2)
x = multipy1(4, 1)
print(x)


def multiply(x, y=0):
    print("value of x=", x)
    print("value of y=", y)

    return x * y

print(multiply(y=2, x=4))


def psr12(p,q):
    return p * q

t = psr12(5,2)

print(t)

def psr1(o):
    return o * o

t = psr1(5)

print(t)

