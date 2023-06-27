a = [1,2,4,5,6,7]
def get_missing_simulation(a):
    n = a[-1]  # n = 7
    sum1 = 0
    total = n*(n+1)//2
    sum1 = sum(a)
    print(total-sum1)


get_missing_simulation(a)


lst=[1,3,5,6,7,8,20]
def missing_no(lst):
    list1=[]
    for i in range(1,lst[-1]):
        if i not in lst:
            list1.append(i)
        i = i+1
    print(list1)

missing_no(lst)

b = [9,1,2,4,5,7,8]

def missing_nos(b):
    b.sort()
    ln_no = b[-1]
    mss_no = []
    for i in range(1,ln_no+1):
        if i not in b:
            mss_no.append(i)

    print(mss_no)


missing_nos(b)