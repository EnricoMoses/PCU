# Buat list kosong untuk menampung matriks
matriks = []

# Loop untuk meminta input 3 baris
for i in range(3):
    # Minta input satu baris angka yang dipisahkan spasi
    input_baris = input(f"Masukkan 3 angka (dipisahkan spasi) untuk baris {i+1}: ")

    # Pisahkan string berdasarkan spasi dan ubah setiap elemen menjadi integer
    # List comprehension digunakan di sini untuk cara yang lebih efisien
    baris = [int(angka) for angka in input_baris.split()]

    # Tambahkan baris yang sudah diproses ke dalam matriks
    matriks.append(baris)

# Cetak matriks
print("\nMatriks yang dibuat adalah:")
for baris in matriks:
    print(baris)
# menampilkan per sel di matriks
# Perulangan luar untuk setiap baris
for baris in matriks:
    # Perulangan dalam untuk setiap sel (elemen) di dalam baris
    for sel in baris:
        # Cetak setiap sel, diakhiri dengan spasi (bukan baris baru)
        print(sel, end=" ")
    # Cetak baris baru setelah semua sel dalam satu baris selesai dicetak
    print()
# menampilkan menggunakan indeks
for i in range(len(matriks)):
    # Dapatkan jumlah kolom pada baris saat ini
    jumlah_kolom = len(matriks[i])

    # Perulangan dalam untuk indeks kolom (j)
    for j in range(jumlah_kolom):
        # Akses elemen menggunakan indeks matriks[i][j]
        sel = matriks[i][j]
