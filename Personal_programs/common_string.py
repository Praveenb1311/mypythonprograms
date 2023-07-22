def common_letters():
    str1 = input("Please enter the first string: ")
    str2 = input("Please enter the second string: ")
    print(type(str2))
    s1 = set(str1.upper())
    s2 = set(str2.upper())
    print(s1)
    print(s2)
    common_let = (s1 & s2)
    print("The common letter for the both the strings : ", common_let)


common_letters()


#2nd Method:

def common_letters():
    str1 = input("Please enter the first string: ")
    str2 = input("Please enter the second string: ")

    s1 = set(str1.upper())
    s2 = set(str2.upper())
    ps1 = set(list(s1))
    s2 = set(list(s2))

    common = list(s1.intersection(s2))
    print(common)


common_letters()


