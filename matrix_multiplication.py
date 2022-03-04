<<<<<<< HEAD
#
# def Principal_Diagonal(matrix, n):
#     print("Principal Diagonal: ", end="")
#     diagonal_element =[]
#     for i in range(n):
#      for j in range(n):
#         if (i == j):
#             diagonal_element.append(matrix[i][j])
#     return diagonal_element
#
#
# def Secondary_Diagonal(matrix, n):
#     print("Secondary Diagonal: ", end="")
#     sec_diagonal_element = []
#     for i in range(n):
#         for j in range(n):
#             if ((i + j) == (n - 1)):
#                 sec_diagonal_element.append(matrix[i][j])
#
#     return sec_diagonal_element



# n = 4
#
# a = [[1, 2, 3, 4],
#
#      [5, 6, 8, 8],
#
#      [1, 2, 3, 4],
#
#      [5, 6, 7, 8]]
#
# diagonal_element = Principal_Diagonal(a,n)
# sec_diagonal_element = Secondary_Diagonal(a,n)
# # print(abs(sum(diagonal_element)-sum(sec_diagonal_element)))
#
# A = [2,3,3,4,5,13,14,11]
# # 3 = 55
# # 3 = 60
# 5 =70
# 10 = 80
# # 3 = 45
# # 11 = 90
# total_sum = 0
# for i in range(len(A)):
#     n,m  = input().split()
#     n,m = int(n),int(m)
#     if n in A:
#         total_sum += m
#         A.remove(n)
# print(total_sum)
#

# huli 10 90 99
# praveen 15 4 25
# gauda 4 25 85
# gouda
n = 3
students = []
for i in range(n):
    name,m1,m2,m3 = input().split()
    students.append([name,m1,m2,m3])
name = input("enter the name")
for student in students:
    if student[0] == name:
        average = (int(student[1])+int(student[2])+int(student[3]))/3
        print("{:.2f}".format(average))

        break


Assignment:


=======

def Principal_Diagonal(matrix, n):
    print("Principal Diagonal: ", end="")
    diagonal_element =[]
    for i in range(n):
     for j in range(n):
        if (i == j):
            diagonal_element.append(matrix[i][j])
    return diagonal_element


def Secondary_Diagonal(matrix, n):
    print("Secondary Diagonal: ", end="")
    sec_diagonal_element = []
    for i in range(n):
        for j in range(n):
            if ((i + j) == (n - 1)):
                sec_diagonal_element.append(matrix[i][j])

    return sec_diagonal_element



n = 4

a = [[1, 2, 3, 4],

     [5, 6, 8, 8],

     [1, 2, 3, 4],

     [5, 6, 7, 8]]

diagonal_element = Principal_Diagonal(a,n)
sec_diagonal_element = Secondary_Diagonal(a,n)
print(abs(sum(diagonal_element)-sum(sec_diagonal_element)))
>>>>>>> origin/main
