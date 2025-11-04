R = int(input().strip())
C = int(input().strip())

# Baca grid (tiap baris dipisah spasi)
grid = [input().strip().split() for _ in range(R)]

# DFS rekursif 8-arah untuk menandai semua 'x' yang terhubung
def flood(i, j):
    if i < 0 or i >= R or j < 0 or j >= C or grid[i][j] != 'x':
        return
    grid[i][j] = '#'  # tandai sudah dikunjungi
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di != 0 or dj != 0:
                flood(i + di, j + dj)

# Hitung blob
count = 0
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'x':
            count += 1
            flood(i, j)

print(count)