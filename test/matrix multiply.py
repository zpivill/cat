
rows_a = int(input("Enter the number of rows for matrix A: "))
cols_a = int(input("Enter the number of columns for matrix A: "))


rows_b = int(input("Enter the number of rows for matrix B: "))
cols_b = int(input("Enter the number of columns for matrix B: "))


matrix_a = []
print("Enter elements for matrix A:")
for i in range(rows_a):
    row = []
    for j in range(cols_a):
        element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)
    matrix_a.append(row)


matrix_b = []
print("Enter elements for matrix B:")
for i in range(rows_b):
    row = []
    for j in range(cols_b):
        element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)
    matrix_b.append(row)


matrix_c = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
for i in range(rows_a):
    for j in range(cols_b):
        for k in range(cols_a):
            matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]


print("\nMatrix A:")
for row in matrix_a:
    print(" ".join(map(str, row)))


print("\nMatrix B:")
for row in matrix_b:
    print(" ".join(map(str, row)))


print("\nMatrix C:")
for row in matrix_c:
    print(" ".join(map(str, row)))