TipeBarang = ('Makanan', 'Minuman', 'Alat_Tulis', 'Alat_Makan')

Inventory = {}

def input_barang():
    try:
        nama = input('Masukkan nama barang : ').lower()
        if nama in Inventory:
            raise ValueError('Barang sudah ada di inventory')

        jumlah = int(input('Masukkan jumlah stok: '))
        if jumlah < 0:
            raise ValueError('Jumlah stok tidak valid')

        harga = float(input('Masukkan harga : '))
        if harga < 0:
            raise ValueError('Harga tidak valid')

        print('Pilih tipe barang')
        for i, t in enumerate(TipeBarang):
            print(f'{i}. {t}')
        idx = int(input('Masukkan index tipe barang: '))
        tipe = TipeBarang[idx]

        Inventory[nama] = {
            'jumlah_stok': jumlah,
            'harga_rata': harga,
            'tipe_barang': tipe,
        }

        print('Barang berhasil ditambahkan')
    except IndexError:
        print('Index tipe barang tidak valid')
    except ValueError as e:
        print(e)


def pembelian_barang():
    try:
        nama = input('Input nama barang : ')
        if nama not in Inventory:
            raise ValueError('Barang tidak ada di inventory')

        beli = int(input('Input kuantitas beli: '))
        harga_beli = float(input('Input harga beli: '))

        data = Inventory[nama]
        stok_lama = data['jumlah_stok']
        harga_lama = data['harga_rata']

        stok_baru = stok_lama + beli
        harga_baru = ((stok_lama * harga_lama) +( beli * harga_beli)) / stok_baru

        data['jumlah_stok'] = stok_baru
        data['harga_rata'] = harga_baru

        print('Pembelian berhasil diproses')
    except ValueError as e:
        print(e)

def penjualan_barang():
    try:
        nama = input('Input nama barang : ')
        if nama not in Inventory:
            raise ValueError('Barang tidak ada di inventory')

        jual = int(input('Input jumlah jual: '))
        stok = Inventory[nama]['jumlah_stok']

        if jual > stok:
            raise ValueError('Jumlah stok tidak valid')

        Inventory[nama]['jumlah_stok'] -= jual
        harga_jual = Inventory[nama]['harga_rata'] * 1.05

        print(f'Harga jual per unit: {harga_jual}')

    except ValueError as e:
        print(e)


def lihat_barang():
    pilihan = input('Input nama barang / semua : ').lower()

    if pilihan == 'semua':
        for nama, data in Inventory.items():
            print(nama, data)
    else :
        if pilihan in Inventory:
            print(pilihan, Inventory[pilihan])
        else:
            print('Barang tidak ada di inventory')

def stok_minimum():
    try:
        minimum = int(input('Masukkan minimum stok : '))
        for nama, data in Inventory.items():
            if data['jumlah_stok'] < minimum:
                print(nama, data)
    except ValueError:
        print('Input tidak valid')

while True:
    print('=== MENU INVENTORY ===')
    print('1. Input barang baru')
    print('2. Pembelian barang')
    print('3. Penjualan barang')
    print('4. Lihat data barang')
    print('5. Stock Minimum barang')
    print('6. Exit')

    try:
        pilih = int(input('Masukkan pilihan : '))
        if pilih == 1:
            input_barang()
        elif pilih == 2:
            pembelian_barang()
        elif pilih == 3:
            penjualan_barang()
        elif pilih == 4:
            lihat_barang()
        elif pilih == 5:
            stok_minimum()
        elif pilih == 6:
            print('Program selesai')
            break
        else:
            raise ValueError('Menu tidak valid')
    except ValueError as e:
        print(e)
