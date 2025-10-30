total_belanja = 0

def tambah_barang(harga):
    global total_belanja
    total_belanja += harga
    print(f'Menambah barang seharga Rp{harga}')

def reset_total():
    global total_belanja
    total_belanja = 0

reset_total()
tambah_barang(int(input('Masukkan harga barang 1 : ')))
tambah_barang(int(input('Masukkan harga barang 2 : ')))
tambah_barang(int(input('Masukkan harga barang 3 : ')))
print(f'Total belanja saat ini : Rp{total_belanja}')