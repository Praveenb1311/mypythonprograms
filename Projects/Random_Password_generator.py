import random
import string

total = string.ascii_letters + string.digits + string.punctuation
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

length = 16

password = "".join(random.sample(total, length))

print(password)