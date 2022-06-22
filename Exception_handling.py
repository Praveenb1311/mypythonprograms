print("Division")
n = int(input("enter n: "))
m = int(input("enter m: "))
# try catch methodology
try:
    x = m / n
    print("{}/{}={}".format(m, n, x))
except Exception as e:
    print(e)


else:
    print("this will execute if there is no error")


finally:
    print("This will always execute")



print("Multiplication")

x = m * n

print("{}*{}={}".format(m,n,x))

with open("hello.txt","w") as fp:
    fp.write("This is my fist time writing to a file")
    fp.write("\n\nThis is my second time time writing to a fil