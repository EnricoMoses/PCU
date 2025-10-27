pelanggan_lain = ''
while pelanggan_lain != 'n':
    kode = int(input('Masukkan kode barang (1-3):'))
    jumlah = int(input('Masukkan jumlah barang: '))
    harga = 0
    if kode == 1:
        harga = 5_000
    elif kode == 2:
        harga = 7_500
    elif kode == 3:
        harga = 10_000

    total = jumlah * harga
    print(f'Total sebelum diskon: {total}')
    if total > 50_000:
        print('Diskon 10% diterapkan')
        total_diskon = total - (total * 0.1)
        print(f'Total yang harus dibayar: {int(total_diskon)}')
    else:
        print(f'Total yang harus dibayar: {total}')

    while pelanggan_lain != 'n' and pelanggan_lain != 'y':
        pelanggan_lain = input('Apakah ada pelanggan lain? (y/n):')
        print()

    if pelanggan_lain == 'n':
        break
