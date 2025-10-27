inp1 = input().split()
n = int(inp1[0]) # baris matrix 1
m = int(inp1[1]) # kolom matrix 2
x = int(inp1[2]) # kolom matrix 1 dan baris matrix 2
matrix1 = []
for k in range(n):
    temp = []
    inp3 = input().split()
    for l in range(x):
        temp.append(int(inp3[l]))
    matrix1.append(temp)

matrix2 = []

for o in range(x):
    temp = []
    inp3 = input().split()
    for p in range(m):
        temp.append(int(inp3[p]))
    matrix2.append(temp)

for i in range(n):
    baris_baru = []
    for j in range(m):
        total = 0
        for k in range(x):
            total += matrix1[i][k] * matrix2[k][j]
        baris_baru.append(str(total))
    print(' '.join(baris_baru))
