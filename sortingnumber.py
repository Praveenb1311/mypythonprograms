# def sort_letter(letter):
#     for i in range(letter):
#         for j in range(i+1,letter):
#             if letter[i] < letter[j]:
#                 tmp = letter[i]
#                 letter[i] = letter[j]
#                 letter[j] = letter[i]
#     return letter
#
# print(sort_letter("complication"))
# def sort_letter(letter):
#     return "".join(sorted(letter))
#
# print(sort_letter("complications"))

def sort_letter(letter):
    return "".join(sorted(letter,reverse=True))

print(sort_letter("complications"))

