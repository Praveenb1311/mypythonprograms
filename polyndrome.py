def check_polyndrome(str1):
    rev_str=""
    for i in range (len(str1)):
        rev_str +=str1[-i-1]
    if str1 == rev_str:
        return True
    else:
        return False

#     for i in range (len(str1)//2):
#         # print(i, -i - 1)
#         if str1[i] != str1[-i-1]:
#
#             return False
#     return True
#
print(check_polyndrome("madam"), "madam")
print(check_polyndrome("malayalam"), "malayalam")
print(check_polyndrome("sms"))
print(check_polyndrome("dad"))
print(check_polyndrome("sister"))
print(check_polyndrome("doddahulugppa"))
print(check_polyndrome("abba"))
print(check_polyndrome("a"))


