list2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for i in range(len(list2d)):
    for j in range(len(list2d[0])):
        print(list2d[i][j], end=' ')
    print()

list_tambah = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

hasil = []
for i in range(len(list_tambah)):
    baris = []
    for j in range(len(list_tambah[0])):
        baris.append(list2d[i][j] + list_tambah[i][j])
    hasil.append(baris)

print('\nHasil Penjumlahan :')
for i in range(len(hasil)):
    for j in range(len(hasil[0])):
        print(hasil[i][j], end=' ')
    print()

# Perkalian matrix elemen per elemen
if len(list2d) == len(list_tambah) and len(list2d[0]) == len(list_tambah[0]):
    hasil_perk_el = []
    for i in range(len(list2d)):
        baris = []
        for j in range(len(list2d[0])):
            baris.append(list2d[i][j] * list_tambah[i][j])
        hasil_perk_el.append(baris)

    print('\nHasil Perkalian elemen-per-elemen :')
    for i in range(len(hasil_perk_el)):
        for j in range(len(hasil_perk_el[0])):
            print(hasil_perk_el[i][j], end=' ')
        print()

else:
    print('\nTidak bisa Perkalian elemen-per-elemen : ukuran matrix berbeda')

# Perkalian matrixs (dot produk)
baris_a, kolom_a = len(list2d), len(list2d[0])
baris_b, kolom_b = len(list_tambah), len(list_tambah[0])

if kolom_a == baris_b:
    hasil_kali_matrix = []
    for i in range(baris_a):
        baris = []
        for j in range(kolom_b):
            # hitung elemen (i, j)
            total = 0
            for k in range(kolom_a): # atau range(baris_b)
                total += list2d[i][k] * list_tambah[k][j]
            baris.append(total)
        hasil_kali_matrix.append(baris)

    print('\nHasil Perkalian matrix (dot product)')
    for i in range(len(hasil_kali_matrix)):
        for j in range(len(hasil_kali_matrix[0])):
            print(hasil_kali_matrix[i][j], end=' ')
        print()

else:
    print('\nTidak bisa melakukan perkalian matrix: jumlah kolom matrix pertama harus sama dengan baris matrix kedua')

