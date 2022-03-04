
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