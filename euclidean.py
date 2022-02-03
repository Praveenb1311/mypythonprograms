matrix_a = [[1,2],[3,4]]
matrix_b = [[4,5],[6,7]]
# matrix_c = [[5,7], [9,11]]
matrix_c = []
for i in range(2):
    temp_array = []
    for j in range(2):
        temp_array.append(matrix_a[i][j] + matrix_b[i][j])
        # print(temp_array)
    matrix_c.append(temp_array)
print(matrix_c)

# matrix_c = [[0,0]*2]
# for i in range(len(matrix_a)):
#     temp_array = []
#     for j in range(len(matrix_a[0])):
#         # if i == j:
#         #     print(i,j)
#         matrix_c[i][j] = matrix_a[i][j] + matrix_b[i][j]
# print(matrix_c)
#

