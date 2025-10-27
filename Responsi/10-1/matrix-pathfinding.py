A = [
    [2, 3, 1],
    [-5, 10, 4],
    [3, -1, 2]
]

tinggi = len(A)
lebar = len(A[0])

B = [[0] * lebar for _ in range(tinggi)]


for i in range(tinggi):
    for j in range(lebar):
        if i == 0 and j == 0:
            B[i][j] = A[i][j]
        elif i == 0:
            B[i][j] = B[i][j - 1] + A[i][j]
        elif j == 0:
            B[i][j] = B[i - 1][j] + A[i][j]
        else:
            B[i][j] = min(B[i - 1][j], B[i][j - 1]) + A[i][j]

for i in range(tinggi):
    for j in range(lebar):
        print(B[i][j], end="\t")
    print()

