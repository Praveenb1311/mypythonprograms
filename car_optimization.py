# # group of frds- located in a point - gather at a meeting - looking for adjustment for available seats
#
# P = [2,3,1,5]
# S = [4,2,5,8]
#
# total_persons = sum(P)
# S.sort(reverse = True)
# temp_sum = 0
# count = 1
# for s in S:
#     temp_sum += s
#     if temp_sum >= total_persons:
#         break
#     count += 1
#
# print(count)


P = [2,3,1,10]
S = [4,2,16,3]

total_persons = sum(P)
print(total_persons)
temp_sum = 0
count = 1
while(True):
    max_seat = max(S)
    temp_sum += max_seat
    S.remove(max_seat)
    if temp_sum >= total_persons:
        break
    elif temp_sum + min(S) >= total_persons:
        count = count+1
        temp_sum += min(S)
        break
    else:
        count += 1

print(count)
# print(temp_sum)
