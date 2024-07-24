def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(4, 6, 45)
result3 = get_matrix(5, 2, 15)
print(result1)
print(result2)
print(result3)

