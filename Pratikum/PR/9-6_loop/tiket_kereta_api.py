print('=== Pemesanan Tiket Kereta Api ===')
tujuan = int(input('''Tujuan:
1. Jakarta–Bandung
2. Surabaya–Malang
3. Jogja–Solo
Pilihan: '''))

kelas = int(input('''
Kelas:
1. Ekonomi
2. Bisnis
3. Eksekutif
Pilihan: '''))

kategori_penumpang = int(input('''
Kategori penumpang:
1. Dewasa
2. Anak
3. Lansia
Pilihan: '''))

jumlah_tiket = int(input('\nJumlah tiket: '))
hari_perjalanan = int(input('Hari perjalanan (1=Senin ... 7=Minggu): '))
level_member = int(input('''Level Member:
1. Silver
2. Gold
3. Platinum
4. Non-member
Pilihan: '''))

harga_dasar = 0
harga_normal = 0
if tujuan == 1 :
    tujuan = 'Jakarta-Bandung'
    harga_dasar = 100_000
elif tujuan == 2 and hari_perjalanan != 7:
    tujuan = 'Surabaya-Malang'
    harga_dasar = 120_000
elif tujuan == 3 and (hari_perjalanan == 5 or hari_perjalanan == 6 or hari_perjalanan == 7) :
    tujuan = 'Jogja-Solo'
    harga_dasar = 80_000
else :
    print('Tujuan atau hari perjalanan tidak valid')
    exit()

if kelas == 1:
    kelas = 'Ekonomi'
    harga_normal = harga_dasar + 0
elif kelas == 2 :
    kelas = 'Bisnis'
    harga_normal = harga_dasar + 50_000
elif kelas == 3 :
    kelas = 'Eksekutif'
    harga_normal = harga_dasar + 100_000
else :
    print('Kelas tidak valid')
    exit()

if kategori_penumpang == 1:
    kategori_penumpang = 'Dewasa'
    harga_tiket_per_orang = harga_normal
elif kategori_penumpang == 2 :
    kategori_penumpang = 'Anak'
    harga_tiket_per_orang = harga_normal - (harga_normal * 0.5)
elif kategori_penumpang == 3 :
    kategori_penumpang = 'Lansia'
    harga_tiket_per_orang = harga_normal - (harga_normal * 0.3)
else :
    print('Kategori penumpang tidak valid')
    exit()

total_awal = harga_tiket_per_orang * jumlah_tiket

# Bonus Member
harga_bonus_member = total_awal
if level_member == 1:
    level_member = 'Silver'
    harga_bonus_member = total_awal - (total_awal * 0.05)
elif level_member == 2 :
    level_member = 'Gold'
    harga_bonus_member = total_awal - (total_awal * 0.1)
elif level_member == 3 :
    level_member = 'Platinum'
    harga_bonus_member = total_awal - (total_awal * 0.15)
elif level_member == 4 :
    level_member = 'Non-member'
    harga_bonus_member = total_awal
else :
    print('Member tidak valid')
    exit()

total_bayar = harga_bonus_member
if jumlah_tiket > 5 :
    total_bayar = total_bayar - (total_bayar * 0.15)

if hari_perjalanan == 1:
    hari_perjalanan = 'Senin'
elif hari_perjalanan == 2 :
    hari_perjalanan = 'Selasa'
elif hari_perjalanan == 3 :
    hari_perjalanan = 'Rabu'
elif hari_perjalanan == 4 :
    hari_perjalanan = 'Kamis'
elif hari_perjalanan == 5 :
    hari_perjalanan = 'Jumat'
    total_bayar = total_bayar - 20_000
elif hari_perjalanan == 6 :
    hari_perjalanan = 'Sabtu'
elif hari_perjalanan == 7 :
    hari_perjalanan = 'Minggu'
    total_bayar = total_bayar + (5_000 * jumlah_tiket)
else :
    print('Hari perjalanan tidak valid')
    exit()


# Output
print(f'''
Tujuan        : {tujuan}
Kelas         : {kelas}
Kategori      : {kategori_penumpang}
Jumlah tiket  : {jumlah_tiket}
Hari          : {hari_perjalanan}
Member        : {level_member}
Harga tiket per orang : Rp{int(harga_tiket_per_orang)}
Total awal            : Rp{int(total_awal)}
Total bayar           : Rp{int(total_bayar)}
''')

