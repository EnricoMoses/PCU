matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

l, r = 0, len(matrix) - 1
while l < r:
    for i in range(r - l):
        top, bottom = l, r

#        menyimpan nilai kiri atas
        topLeft = matrix[top][l + i]

#         memindahkan kiri bawah ke kiri atas
        matrix[top][l + i] = matrix[bottom - i][l]

        # memindahkan kanan bawah ke kiri bawah
        matrix[bottom - i][l] = matrix[bottom - i][r - i]

        # memindahkan kanan atas ke kanan bawah
        matrix[bottom][r - i] = matrix[top + i][r]

        # memindahkan kiri atas ke kanan atas
        matrix[top + i][r] = topLeft

    r -= 1
    l += 1

for i in matrix:
    print(*i)