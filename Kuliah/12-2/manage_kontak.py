def tambah_kontak(buku, nama, nomor):
    nama = nama.strip().title()
    nomor = nomor.strip()

    try:
        int(nomor)
    except ValueError:
        print('Nomor harus berupa angka')
        return

    buku[nama] = nomor
    print('Kontak berhasil di tambahkan')

def hapus_kontak(buku, nama):
    target = nama.strip().lower()

    key_ditemukan = None
    for key in buku.keys():
        if key.lower() == target:
            key_ditemukan = key
            break

    if key_ditemukan is None:
        print('Kontak tidak ada')
    else:
        del buku[key_ditemukan]
        print('Kontak berhasil di hapus')


def cari_kontak(buku, keyword):
    kw = keyword.strip().lower()
    hasil = []

    for nama, nomor in buku.items():
        if kw in nama.lower() or kw in nomor.lower():
            hasil.append((nama, nomor))

    return hasil

def tampilkan_buku(buku):
    print('\n--- Daftar Kontak ---')
    if not buku:
        print('(kosong)')
        return

    for nama in sorted(buku.keys(), key=lambda x: buku[x].lower()):
        print(f'{nama} : {buku[nama]}')

buku = {}

while True:
    print("\nMenu:")
    print("1. Tambah Kontak")
    print("2. Hapus Kontak")
    print("3. Cari Kontak")
    print("4. Tampilkan Semua Kontak")
    print("5. Keluar")

    try:
        pilih = int(input('Pilih menu: '))
    except ValueError:
        print('Menu harus berupa angka (1-5)')
        continue

    if pilih == 1:
        nama = input('\nMasukkan nama: ')
        nomor = input('Masukkan nomor: ')
        tambah_kontak(buku, nama, nomor)

    elif pilih == 2:
        nama = input('\nMasukkan nama yang mau di hapus: ')
        hapus_kontak(buku, nama)

    elif pilih == 3:
        keyword = input('\nMasukkan keyword (nama/nomor): ')
        hasil = cari_kontak(buku, keyword)

        if not hasil:
            print('Hasil tidak ada')
        else:
            print('\n--- Hasil Pencarian ---')
            for nama, nomor in hasil:
                print(f'{nama} : {nomor}')

    elif pilih == 4:
        tampilkan_buku(buku)

    elif pilih == 5:
        tampilkan_buku(buku)
        print('Keluar...')
        break

    else:
        print('Pilihan tidak valid')
