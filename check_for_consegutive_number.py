# def double_letters(string1):
#     for i in range(len(string1)-1):
#         if string1[i] == string1[i+1]:
#             return True
#     return False

def double_letters(string):
    print(list(zip(string,string[1:])))
    return any([a == b for a, b in zip(string, string[1:])])

print(double_letters("hello"))
print(double_letters("nono"))
print(double_letters("appa"))
print(double_letters("praveee"))

