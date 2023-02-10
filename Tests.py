from MatrixVectorFunctions import *
from main import *
from Factorization_LU import *


def gauss_seidel_C(matrix, b):
    x = [1 for i in b]
    res = []
    norm_res = 1.0
    min_norm = 10 ** (-6)
    L = get_L(matrix)
    U = get_U(matrix)
    D = get_D(matrix)
    i = 0
    norms = []
    while norm_res > min_norm and i < 10:
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
        norms.append(norm_res)
        i += 1
    return norms


def jacobi_C(matrix, b):
    x = [1 for i in b]
    res = []
    norm_res = 1.0
    min_norm = 10 ** (-6)
    L = get_L(matrix)
    U = get_U(matrix)
    D = get_D(matrix)
    norms = []
    i = 0
    while norm_res > min_norm and i < 10:
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
        norms.append(norm_res)
        i += 1
    return norms


N = 9 * 4 * 8
a1 = 3
a2 = -1
a3 = -1
matrix = create_matrix(a1, a2, a3, N)
vector = create_vector(4, N)
x = direct_algorithm(matrix, vector)
Ax = multiply_matrix_vector(matrix, x)
res = add_vectors(Ax, [(-1) * el for el in vector])
norm_res = norm(res)
print(norm_res)
# result_jacobi = jacobi_C(matrix, vector)
# result_gauss_seidel = gauss_seidel_C(matrix, vector)
# print(result_jacobi)
# print()
# print(result_gauss_seidel)
