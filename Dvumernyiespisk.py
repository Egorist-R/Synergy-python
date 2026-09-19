import random

def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            random_number = random.randint(-100, 100)
            row.append(random_number)
        matrix.append(row)
    return matrix

def sum_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    matrix_res = []
    for i in range(rows):
        row_res = []
        for j in range(cols):
            total = matrix_a[i][j] + matrix_b[i][j]
            row_res.append(total)
        matrix_res.append(row_res)
    return matrix_res

COUNT_ROWS = 10 
COUNT_COLS = 10

matrix_1 = create_matrix(COUNT_ROWS, COUNT_COLS)
matrix_2 = create_matrix(COUNT_ROWS, COUNT_COLS)

matrix_3 = sum_matrices(matrix_1, matrix_2)

print("--- МАТРИЦА 1 ---")
for row in matrix_1:
    print(row)

print("\n--- МАТРИЦА 2 ---")
for row in matrix_2:
    print(row)

print("\n--- РЕЗУЛЬТАТ СЛОЖЕНИЯ (МАТРИЦА 3)--- ")
for row in matrix_3:
    print(row)