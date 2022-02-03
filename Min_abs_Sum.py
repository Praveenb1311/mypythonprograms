my_list1 = [1,2,3,4,5]
my_list2 = [3,3,3,3,3]
my_list3 = [2,1,0,1,2]
sum1 = 6

huli_list1 = [1,2,6,8,10]
huli_list2 = [2,2,2,2,2]
huli_list3 = [1,0,4,6,8]
sum2 = 19
abs_sum_list = []
for number in my_list1:
    abs_sum = [abs(num-number) for num in my_list1]
    abs_sum_list.append(sum(abs_sum))
print(min(abs_sum_list))

abs_sum_list = []
for number in huli_list1:
    abs_difference = [abs(num-number) for num in huli_list1]
    abs_sum_list.append(sum(abs_difference))
    print(abs_difference)
print(min(abs_sum_list))
print(abs_sum_list)



list1 = []
for j in range(10):
    list1.append(j)
print("list1 : ", list1 )
list2 = [j for j in range(10)]# list comphrension
print("list2 : ", list2 )

# triplets ex 3,4,5

# to find number of triplets below 100

for z in range(100):
    for y in range(1,z):
        for x in range(1,y):
            if x*x + y*y == z*z:
                print(x,y,z)

triplets = ((x,y,z) for z in range(100) for y in range(1,z) for x in range(1,y) if x*x + y*y == z*z)
# print(tuple(triplets))




