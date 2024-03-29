import time
from calendar import isleap

def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False

# print(judge_leap_year(2000))

def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28

name = input("Enter your name: ")
age = input("Enter your age: ")

local_time = time.localtime(time.time())
# print(local_time)
year = int(age)

month = year * 12 + local_time.tm_mon
day = 0

begin_year = int(local_time.tm_year) - year
end_year = begin_year + year

for y in range(begin_year,end_year):
    if (judge_leap_year(y)):
        day = day + 366
    else:
        day = day + 365

leap_year = judge_leap_year(local_time.tm_year)
for m in range(1, local_time.tm_mon):
    day = day + (month_days(m, leap_year))

day = day + local_time.tm_year
print("{}'s age is {} years or ".format(name, year), end ="")
print("{} months or {} days".format(month, day))

