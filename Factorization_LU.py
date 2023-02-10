from copy import deepcopy
from MatrixVectorFunctions import *


def matrix_factorization_LU(matrix):
    N = len(matrix)
    U = deepcopy(matrix)
    L = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        L[i][i] = 1

    for k in range(N - 1):
        for j in range(k + 1, N):
            L[j][k] = U[j][k] / U[k][k]
            for i in range(k, N):
                U[j][i] = U[j][i] - L[j][k] * U[k][i]

    return L, U


def direct_algorithm(matrix, b):
    L, U = matrix_factorization_LU(matrix)
    y = solve_L_equation(L, b)
    x = solve_U_equation(U, y)
    return x
