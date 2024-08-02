def matrix_multiply(X, Y):
    result = [[0 for _ in range(len(Y[0]))] for _ in range(len(X))]

    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    return result

# Example matrices
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

result_matrix = matrix_multiply(matrix1, matrix2)
for row in result_matrix:
    print(row)
