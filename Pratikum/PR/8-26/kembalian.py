uang_dibayar = int(input('Uang dibayar: '))

jumlah_barang1 = int(input('Jumlah barang 1: '))
harga_barang1 = int(input('Harga barang 1: '))

jumlah_barang2 = int(input('Jumlah barang 2: '))
harga_barang2 = int(input('Harga barang 2: '))

jumlah_barang3 = int(input('Jumlah barang 3: '))
harga_barang3 = int(input('Harga barang 3: '))

total_belanja = (jumlah_barang1 * harga_barang1) +(jumlah_barang2 * harga_barang2) +(jumlah_barang3 * harga_barang3)
uang_kembalian = uang_dibayar - total_belanja

sisa = uang_kembalian

lembar_20_000 = sisa // 20_000
sisa = sisa % 20_000

lembar_10_000 = sisa // 10_000
sisa = sisa % 10_000

lembar_5_000 = sisa // 5_000
sisa = sisa % 5_000

lembar_2_000 = sisa // 2_000

print(f'Uang kembalian yang diterima adalah Rp.{uang_kembalian}, dengan rincian:')

print(f'2.000 : {lembar_2_000} lembar')
print(f'5.000 : {lembar_5_000} lembar')
print(f'10.000 : {lembar_10_000} lembar')
print(f'20.000 : {lembar_20_000} lembar')



