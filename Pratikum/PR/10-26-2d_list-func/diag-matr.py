def diagonal_utama(matriks):
    n = len(matriks)
    return sum(matriks[i][i] for i in range(n))

def diagonal_sekunder(matriks):
    n = len(matriks)
    return sum(matriks[n-1-i][i] for i in range(n))

n = int(input())

matriks = []
for _ in range(n):
    row = list(map(int, input().split()))
    matriks.append(row)

jumlah_utama = diagonal_utama(matriks)
jumlah_sekunder = diagonal_sekunder(matriks)

print(f'Jumlah diagonal utama: {jumlah_utama}')
print(f'Jumlah diagonal sekunder: {jumlah_sekunder}')