produk = int(input('Pilih produk (1: Soda - 10.000, 2: Snack - 5.000): '))
jumlah_barang = int(input('Jumlah: Masukkan jumlah barang yang ingin dibeli: '))

# Proses menghitung harga total
harga_total = 0
if produk == 1:
    harga_total = 10_000 * jumlah_barang
    nama_produk = 'Soda'
elif produk == 2:
    harga_total = 5_000 * jumlah_barang
    nama_produk = 'Snack'
else:
    print('Produk tidak ditemukan')

print(f'– Harga total belanja {harga_total} –')

isCukup = False
temp = harga_total
while not isCukup:
    uang = int(input('Masukkan uang: '))
    sisa = temp - uang
    if sisa == 0:
        isCukup = True
        print(f'Transaksi berhasil, selamat menikmati {jumlah_barang} {nama_produk}!')
    elif sisa < 0:
        isCukup = True
        print(f'Transaksi berhasil, selamat menikmati 2 Snack! Uang kembalian Anda Rp {abs(sisa)}')
    else:
        print('Uang tidak cukup, silahkan tambahan.')
        temp = sisa

