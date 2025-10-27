while True:
    n = int(input('Masukkan bilangan ganjil (>=5): '))
    if n % 2 == 1 and n >= 5:
        break

for i in range(n):
    for j in range(n):
        atas = i
        kiri = j
        bawah = n - 1 - i
        kanan = n - 1 - j

        # m = atas
        # if kiri < m: m = kiri
        # if bawah < m: m = bawah
        # if kanan < m: m = kanan

        m = min(atas, kiri, bawah, kanan)

        nilai = 1 + m
        print(nilai, end=' ')
    print()
