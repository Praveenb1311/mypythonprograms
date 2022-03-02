#kang_0(0 pos 3m )
#kang_1(2m 5th position)3

k1 = 0
k1_speed = 3
k2 = 4
k2_speed = 2
initial_distance = k2-k1
new_distance = (k2 + k2_speed) - (k1 + k1_speed)
if new_distance < initial_distance:
    print('yes')
else:
    print("no")

k1 = 0
k1_speed = 3
k2 = 5
k2_speed = 3
initial_distance = k2-k1
new_distance = (k2 + k2_speed) - (k1 + k1_speed)
if new_distance < initial_distance:
    print('yes')
else:
    print("no")
def kang_problem(k1, k1_speed, k2, k2_speed):
    count = 0
    initial_distance = k2-k1
    while(initial_distance):
        k2 += k2_speed
        k1 += k1_speed
        new_distance = k2 - k1
        if new_distance >= initial_distance:
            break
        else:
            count += 1
            initial_distance = new_distance
    if count:              #if count is not equal to zero and if not count means coint == 0
        print("meets at {} jumps".format(count))
    else:
        print("never meet")


kang_problem(0, 3, 5, 3)
kang_problem(0, 3, 5, 2)
kang_problem(0, 3, 4, 2)