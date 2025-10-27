print('=== MATTHEW"S Cafe ===')
nama = input('nama: ')

pesanan = 1

jml_americano = 0
jml_latte = 0
jml_fries = 0

while pesanan != 0:
    pesanan = int(input('''
Pesan Makanan:
1. Americano: Rp 32,000
2. Latte Rp 46,000
3. French Fries Rp 28,000
0. Keluar
Pilihan Anda: '''))

    if pesanan == 1:
        jml_americano += 1
        print('Americano telah ditambahkan.')
    elif pesanan == 2:
        jml_latte += 1
        print('Latte telah ditambahkan.')
    elif pesanan == 3:
        jml_fries += 1
        print('French Fries telah ditambahkan.')
    elif pesanan == 0:
        break
    else:
        print('Kode makanan tidak valid')

print(f'\nTerima kasih Singgih! Kami akan segera proses pesanan Anda dengan detail sebagai berikut:')

total = 0
if jml_americano > 0:
    print(f'{jml_americano}x Americano @Rp 32,000')
    total += jml_americano * 32_000
if jml_latte > 0:
    print(f'{jml_latte}x Latte @Rp 46,000')
    total += jml_latte * 46_000
if jml_fries > 0:
    print(f'{jml_fries}x Fries @Rp 28,000')
    total += jml_fries * 28_000

print(f'Total Rp {total:,}')
print('Sampai bertemu kembali.')
