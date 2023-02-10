from math import sqrt
from copy import deepcopy


def get_L(matrix):
    n = len(matrix)
    new_matrix = [[0 for i in range(n)] for j in range(n)]
    for j, row in enumerate(matrix):
        for i, value in enumerate(row):
            if i >= j:
                break
            new_matrix[j][i] = value
    return new_matrix


def get_U(matrix):
    diag_index = 0
    n = len(matrix)
    new_matrix = [[0 for i in range(n)] for j in range(n)]
    for j, row in enumerate(matrix):
        for i, value in enumerate(row):
            if i <= diag_index:
                continue
            new_matrix[j][i] = value
        diag_index += 1
    return new_matrix


def get_D(matrix):
    n = len(matrix)
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        new_matrix[i][i] = matrix[i][i]
    return new_matrix


def multiply_matrix_vector(matrix, vector):
    n = len(matrix)
    new_vector = [0 for _ in range(n)]
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            new_vector[i] += matrix[i][j] * vector[j]
    return new_vector


def multiply_matrix_value(matrix, value):
    new_matrix = deepcopy(matrix)
    for i, row in enumerate(new_matrix):
        for j, element in enumerate(row):
            new_matrix[i][j] = element * value
    return new_matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


def add_martix(matrix1, matrix2):
    new_matrix = deepcopy(matrix1)
    for i, row in enumerate(matrix2):
        for j, element in enumerate(row):
            new_matrix[i][j] += element
    return new_matrix


def add_vectors(vecor1, vector2):
    new_vector = [el for el in vecor1]
    for i, element in enumerate(vector2):
        new_vector[i] += element
    return new_vector


def norm(vector):
    x = 0.0
    for element in vector:
        x += element ** 2
    return sqrt(x)


def check_zero_on_diagonal(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            return i
    return -1


def remove_zero_from_diagonal(matrix, vector, zero_index):
    new_matrix = []
    new_vector = deepcopy(vector)
    for i, element in enumerate(matrix[zero_index]):
        if element != 0 and matrix[i][zero_index] != 0:
            new_vector[i], new_vector[zero_index] = new_vector[zero_index], new_vector[i]
            if i < zero_index:
                new_matrix = matrix[:i] + [matrix[zero_index]] + matrix[i + 1:zero_index] + [matrix[i]]
                if zero_index < len(matrix):
                    new_matrix += matrix[(zero_index + 1):]
            else:
                new_matrix = matrix[:zero_index] + [matrix[i]] + matrix[zero_index + 1:i] + [matrix[zero_index]]
                if i < len(matrix):
                    new_matrix += matrix[(i + 1):]
            return new_matrix, new_vector
    return matrix, vector


def solve_diagonal_equation(D, vector):
    result = []
    for i in range(len(D)):
        result.append(vector[i] / D[i][i])
    return result


def solve_L_equation(matrix_p, vector_p):
    matrix = deepcopy(matrix_p)
    vector = deepcopy(vector_p)
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            matrix, vector = remove_zero_from_diagonal(matrix, vector, i)
        diag_val = matrix[i][i]
        for j, val in enumerate([x[i] for x in matrix]):
            if j <= i:
                continue
            matrix[j][i] = 0
            vector[j] = vector[j] - (val * vector[i]) / matrix[i][i]
    result = solve_diagonal_equation(matrix, vector)
    return result


def solve_U_equation(matrix_p,vector_p):
    matrix = deepcopy(matrix_p)
    vector = deepcopy(vector_p)
    N = len(matrix)
    for i in reversed(range(N)):
        if matrix[i][i] == 0:
            matrix, vector = remove_zero_from_diagonal(matrix, vector, i)
        j = N - 1
        for val in reversed([x[i] for x in matrix]):
            if j >= i:
                j -= 1
                continue
            matrix[j][i] = 0
            vector[j] = vector[j] - (val * vector[i]) / matrix[i][i]
            j -= 1
    result = solve_diagonal_equation(matrix,vector)
    return result
