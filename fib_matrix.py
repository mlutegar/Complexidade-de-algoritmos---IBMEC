import numpy as np


def fib_matrix(n):
    def matrix_mult(A, B):
        return np.dot(A, B).astype(object)

    def matrix_exponentiation(matrix, exp):
        result = np.identity(len(matrix), dtype=object)
        while exp:
            if exp % 2:
                result = matrix_mult(result, matrix)
            matrix = matrix_mult(matrix, matrix)
            exp //= 2
        return result

    F = np.array([[1, 1], [1, 0]], dtype=object)
    return matrix_exponentiation(F, n - 1)[0][0] if n > 0 else 0
