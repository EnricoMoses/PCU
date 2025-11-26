s = input().strip()        # contoh: "3+2+1"

# ambil hanya angkanya (1, 2, 3)
angka = [ch for ch in s if ch != '+']

# urutkan naik
angka.sort()

# gabungkan lagi dengan '+'
hasil = '+'.join(angka)

print(hasil)
