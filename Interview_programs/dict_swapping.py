
# Sort dictionary by values

dict = {"math": 54, "Eng": 45, "Sce":67, "Hin": 55}

dict1 = {}
temp = {}

for key,value in dict.items():
    temp[value] = key
print(temp)

for key in sorted(temp.keys()):
    dict1[key] = temp[key]

print(dict1)
prave = {}
for value,key in dict1.items():
    prave[key] = value

print(prave)

# Sort dictionary by keys

pic = {"A":1, "B": 6, "C": 3, "R": 5, "F": 23, "L":23}

new_pic = {}

sk = sorted(pic.keys())

print(sk)

for i in sk:
    new_pic[i]=pic[i]


print(new_pic)

dict2 = {"math": 54, "Eng": 45, "Sce":67, "Hin": 55}

new_dict2 = {}

sk1 = sorted(dict2.keys())
print(sk1)

for i in sk1:
    new_dict2[i] = dict2[i]

print(dict2)