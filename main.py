from math import sin

from Gauss_Seidel import gauss_seidel
from Jacobi import jacobi


def create_matrix(a1, a2, a3, N):
    matrix = [[0 for i in range(N)] for j in range(N)]

    diag_index = 0

    for row in matrix:
        if diag_index - 2 >= 0:
            row[diag_index - 2] = a3
        if diag_index - 1 >= 0:
            row[diag_index - 1] = a2
        row[diag_index] = a1
        if diag_index + 1 < N:
            row[diag_index + 1] = a2
        if diag_index + 2 < N:
            row[diag_index + 2] = a3

        diag_index += 1

    return matrix


def create_vector(f, N):
    return [sin(i * (f + 1)) for i in range(N)]


if __name__ == '__main__':
    # ----------------------------------------zadanie  A i B ----------------------------------------

    N = 9 * 4 * 8
    a1 = 5 + 8
    a2 = -1
    a3 = -1
    matrix = create_matrix(a1, a2, a3, N)
    vector = create_vector(4, N)
    print(jacobi(matrix, vector))
    print(gauss_seidel(matrix, vector))

    # ----------------------------------------zadanie  C ----------------------------------------
    N = 9 * 4 * 8
    a1 = 3
    a2 = -1
    a3 = -1
    matrix = create_matrix(a1, a2, a3, N)
    vector = create_vector(4, N)
    ##print(jacobi(matrix, vector))
    ##print(gauss_seidel(matrix, vector))
