# A = [
#     [2, 3, 1],
#     [-5, 10, 4],
#     [3, -1, 2]
# ]
#
# tinggi = len(A)
# lebar = len(A[0])
#
# B = [[0] * lebar for _ in range(tinggi)]
#
#
# for i in range(0):
#     for j in range(1, 3):
#         A[i][j] = A[i][j-1]
#
# for i in range(1, 3):
#     for j in range(0):
#         A[i][j] = A[i-1][j]
#
#
# if A[i][j-1] < A[i-1][j-1]:
#
#
# for i in range(tinggi):
#     for j in range(lebar):
#         print(A[i][j], end="\t")
#     print()
#
