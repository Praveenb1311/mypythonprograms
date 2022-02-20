# Runner up score

n = 5
score = []
for i in range(n):
    score.append(int(input("Enter the score"+ str(i+1)+": ")))


#Desiner Door Mat
#minion game

# score.sort(rev
maximum = max(score)
max_counter = score.count(maximum)
while(max_counter):
    score.remove(maximum)
    max_counter -= 1


print(score)
print(max(score))


minimum = min(score)
min_counter = score.count(minimum)
while(min_counter):
    score.remove(minimum)
    min_counter -= 1


print(score)
print(min(score))
# score_1 = score.pop()
# print(score)
