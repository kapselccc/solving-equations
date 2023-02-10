from MatrixVectorFunctions import *


def gauss_seidel(matrix, b):
    x = [1 for i in b]
    res = []
    norm_res = 1.0
    min_norm = 10 ** (-6)
    L = get_L(matrix)
    U = get_U(matrix)
    D = get_D(matrix)
    i = 0
    while norm_res > min_norm:
        # x = - (D + L) \ (Ux) + (D + L) \b
        left = add_martix(D, L)
        left = multiply_matrix_value(left, -1)
        middle = middle = multiply_matrix_vector(U, x)
        left = solve_L_equation(left, middle)
        right = add_martix(D, L)
        right = solve_L_equation(right, b)
        x = add_vectors(left, right)

        # res = Ax - b
        Ax = multiply_matrix_vector(matrix, x)
        res = add_vectors(Ax, [(-1) * el for el in b])
        norm_res = norm(res)
        i += 1

    print("Ended after " + str(i) + " iterations")
    return x
