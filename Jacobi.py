from MatrixVectorFunctions import *


def jacobi(matrix, b):
    x = [1 for i in b]
    res = []
    norm_res = 1.0
    min_norm = 10 ** (-6)
    L = get_L(matrix)
    U = get_U(matrix)
    D = get_D(matrix)
    i = 0
    while norm_res > min_norm:
        # x = D \ (L + U)x + D \ b
        left = add_martix(L, U)
        left = multiply_matrix_vector(left, x)
        left = solve_diagonal_equation(multiply_matrix_value(D, -1), left)
        right = solve_diagonal_equation(D, b)
        x = add_vectors(left, right)

        # res = Ax - b
        Ax = multiply_matrix_vector(matrix, x)
        res = add_vectors(Ax, [(-1) * el for el in b])

        norm_res = norm(res)
        i += 1

    print("Ended after " + str(i) + " iterations")
    return x
