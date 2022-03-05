import itertools

list1 = ["apple","banana","banana","cucumber","biscuits","apple",
         "biscuits","biscuits","apple","biscuits","banana",
         "banana","bana","bana","bana","bana"]
dict_count = {}
for item in list1:
    if item in dict_count:
        dict_count[item] += 1
    else:
        dict_count[item] = 1

print(dict_count)

max_count = max(dict_count.values())
print(max_count)
most_selling_item = [key for key,value in dict_count.items() if value == max_count]

print(most_selling_item)

list2 = [1, 3, 4, 10, 4]
# The summation of list using accumulate is :[1, 4, 8, 18, 22]
result = []
for i in range(len(list2)):
    if i == 0:
        result.append(list2[i])
    else:
        result.append(sum(list2[:i+1]))
print(result)
print(list(itertools.accumulate(list2, lambda x, y: x+y)))