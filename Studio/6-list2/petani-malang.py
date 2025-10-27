inp1 = input().split()
baris = int(inp1[0])
kolom = baris

inp2 = ""
list2d = []
for i in range(baris):
    temp = []
    inp3 = input().split()
    for j in range(kolom):
        temp.append(int(inp3[j]))
    list2d.append(temp)

n = int(inp1[0])

# Ukuran adalah hasil (n-2) x (n-2)
k = n - 2
res = [[0]*k for _ in range(k)]

if n <= 2:
    print(10)
    import sys
    sys.exit()

for i in range(baris):
    for j in range(kolom):
        ii = min(max(i, 1), n - 2) - 1
        jj = min(max(j, 1), n - 2) - 1
        res[ii][jj] += list2d[i][j]

for i in range(k):
    print(*res[i])

