def count_down(start):
    """ Count down from a number  """
    print(start)
    next = start - 1
    if next > 0:
        count_down(next)
count_down(3)


def sum(n):
    total = 0
    for index in range(n+1):
        total = total+index
    return total
result = sum(5)
print(result)

print("Factorial of given number ")


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(6))

"""
6 * factorial(5) ==> 720
5 * factorial(4) ==> 120
4 * factorial(3) ==> 24
3 * factorial(2) ==> 6
2 * factorial(1) ==> 2

"""

print("Fibonacci series")


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


for i in range(10):
    print(fib(i))


def add(n):
    if n == 1:
        return 1
    return n + add(n - 1)


print(add(5))