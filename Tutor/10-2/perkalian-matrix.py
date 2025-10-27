matrix_1 = [
    [1,2,3,4],
    [5,6,7,8],
]

matrix_2 = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
]

for i in range(len(matrix_1)):
    baris_baru = []
    for j in range(len(matrix_2[0])):
        total = 0
        for k in range(len(matrix_2)):
            total += matrix_1[i][k] * matrix_2[k][j]
            baris_baru.append(total)
        print(' '.join(map(str, baris_baru)))
