
import re
num = 7
print(type(num))
num2 = "hello"
# print()
print(len(num2))
print(num2[4])  # if we want to print index or to access index we need to take the from 0
print(num2[:])  # this will run from 1 ( first 2 will remove,other side 2 will keep from left :
num3 = "12mah132ad4eva12pp213"
print(num3.replace('de', ''))
# print(num3.translate({ord(i) : None for i in "abcdefghijklmnopqrstuvwxyz"}))
x = "".join(re.findall("[a-zA-Z]+", num3))
print(x)
print(num3.translate({ord(i) : None for i in x}))  # ord - letter to number

# print("".join(re.findall("[a-zA-Z]+", num3)))

small_alphabets = [chr(i) for i in range(97, 123)]  #ascii code int to convert char
capital_alphabets = [i for i in range(65, 91)]
print("".join(small_alphabets))
print(capital_alphabets)

print(ord("A"))

num4 = "12mah132ad4eva12pp213"
# print(num4.replace('\d+', ''))
print(re.sub('\d+', '', num4))  #d - digit
print(re.sub('\w+', '', num4))  # w - word but it also contains numbers


