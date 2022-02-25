# Runner up score

n = 5
score = []
for i in range(n):
    score.append(int(input("Enter the score"+ str(i+1)+": ")))
n = 5
score = []
for i in range(n):
    score.append(int(input("Enter the score"+ str(i+1)+": ")))
# n = 5
# score = []
# for i in range(n):
#     score.append(int(input("Enter the score"+ str(i+1)+": ")))

# runner score name in alphabetic order

list1 = [["huli",20],["pravi",10],["prakash",30],["puli",20],["guli",15]]

''' output 
huli 
puli
   '''#documentation comment(multiline comment)
score_list = []
for item in list1:
    score_list.append(item[1])
print(score_list)

score_list = list(set(score_list)) # set will remove the repeated element

print(score_list)

score_list.sort(reverse = True)
# print(score_list)
second_max = score_list[1]
names = [item[0] for item in list1 if second_max == item[1]]#list comprension
print("\n".join(names))

s = 10
e = 15
a = 8
o = 18
a_f = [5, 10, -7]
o_f = [14, -8, -10]

new_a_f = [item + a for item in a_f]
new_o_f = [item + o for item in o_f]
print(new_a_f)
print(new_o_f)

my_apples = [item for item in new_a_f if item >= s and item <= e]
my_oranges = [item for item in new_o_f if item >= s and item <= e]

print(len(my_apples), "apple")
print(len(my_oranges))

# score of 5 studen to be round____the new number has to round off to 5
# diff should be less than 3 and should be more than 38

score = [72, 93, 51, 37, 18, 19, 38]
round_off_score = []
for item in score:
    if item <= 37:
        round_off_score.append(item)
    elif 5-(item % 5) < 3:
        round_off_score.append(item + (5 - (item%5)))
    else:
        round_off_score.append(item)
print(score)
print(round_off_score)

