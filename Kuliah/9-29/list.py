nrp = ['c1', 'c2', 'c3']
nama = ['Adi', 'Ani', 'Surya']
nilai = [81, 87, 73]

while True:
    print('\n Menu')
    menu = int(input('''Pilih
1. Untuk Menambahkan Data
2. Untuk Mengganti Data
3. Hapus Data
4. Tampilkan Data
5. Rata-Rata
6. Selesai
Masukkan salah satu: '''))

    if menu == 1:
        print('Input Tambah')
        nama_input = input('Nama: ')
        nama.append(nama_input)
        nrp_input = input('NRP: ')
        nrp.append(nrp_input)
        nilai_input = int(input('Nilai: '))
        nilai.append(nilai_input)
        print(nrp)
        print(nama)
        print(nilai)

    elif menu == 3:
        print('Delete')
        nrp_delete = input('NRP: ')
        index_del = nrp.index(nrp_delete)
        nrp.pop(index_del)
        nama.pop(index_del)
        nilai.pop(index_del)

    elif menu == 2:
        print('Mengganti list')
        ganti_list = input('Masukkan data mana yang ingin diganti : ')
        if ganti_list == 'nrp':
            ganti_nrp = input('NRP yg ingin di ganti: ')
            index_nrp = nrp.index(ganti_nrp)
            nrp_baru = input('Masukkan NRP baru: ')
            nrp[index_nrp] = nrp_baru
            print(nrp)
        elif ganti_list == 'nama':
            ganti_nama = input('NRP yg ingin di ganti: ')
            index_nama = nama.index(ganti_nama)
            nama_baru = input('Masukkan NRP baru: ')
            nama[index_nama] = nama_baru
            print(nama)
        elif ganti_list == 'nilai':
            ganti_nilai = input('Nilai yg ingin di ganti: ')
            index_nilai = nilai.index(ganti_nilai)
            nilai_baru = input('Masukkan Nilai baru: ')
            nilai[index_nilai] = nilai_baru
            print(nilai)

    elif menu == 4:
        print(nrp)
        print(nama)
        print(nilai)

    elif menu == 5:
        total = 0
        for nilai_satuan in nilai:
            nilai_satuan += total
            total = nilai_satuan

        rata_rata = total/len(nilai)
        print(f'Rata-rata nilai adalah {rata_rata:.2f}')

    else:
        break