# minta user mengetik daftar nilai  dalam satu baris
nilai_mahasiswa = input('Masukkan nilai mahasiswa (pisah dengan spasi atau koma): ')
# ubah semua koma menjadi spasi agar pemisah sama, lalu split berdasarkn spasi agar menajdi list
nilai_mahasiswa = nilai_mahasiswa.replace(',', ' ').split()

# buat variabel awal total dan hitung
total = 0
hitung = 0

# loop nilai mahasiswa nya
for nilai_kotor in nilai_mahasiswa:
    # hilangkan spasi, dan kutip satu atau dua jika ada
    nilai_bersih = nilai_kotor.strip().strip("'\"")

    # taruh kode yg berpotensi error disini
    try:
        # jadikan float nilainya
        nilai = float(nilai_bersih)

    #     jika ada yg bukan float, langsung error masuk ke sini
    except ValueError:
        # beri tau user lalu continue ke loop selanjutnya
        print(f"Error: '{nilai_bersih}' bukan angka yang valid.")
        continue

    # jika nilai kurang dr 0, tdk valid
    if nilai < 0:
        # tampilkan tanpa .0 jika bilangan bulat, lalu lanjut ke loop selanjutnya
        tampil = int(nilai) if nilai.is_integer() else nilai
        print(f'Error: Nilai {tampil} tidak boleh negatif.')
        continue

    # jika nilai lebih dr 100 juga tidak valid
    if nilai > 100:
        # tampilkan tanpa .0 jika bilangan bulat, lalu lanjut ke loop selanjutnya
        tampil = int(nilai) if nilai.is_integer() else nilai
        print(f'Error: Nilai {tampil} tidak boleh lebih dari 100.')
        continue

    # jika lolos semua validasi tambahkan ke total
    total += nilai
    # hitung juga jumlah nilai yg valid (utk di bagi, utk mencari rata2)
    hitung += 1

# jika hitung lebih dr nol
if hitung > 0:
    # hitung rata-rata lalu tampilkn 2 angka di blkg koma dan print,
    print(f'Rata-rata nilai valid: {total / hitung:.2f}')
# jika tidak ada nilai sama sekali
else:
    print('Tidak ada nilai valid')

