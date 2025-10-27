menu = [
    ['c1', 'Adi', 81],
    ['c2', 'Ani', 87],
    ['c3', 'Surya', 72]
]

while True:
    for i in range(len(menu)):
        print(f'Nama: {menu[i][1]}\tNRP: {menu[i][0]}\tNilai: {menu[i][2]}')

    pilih = int(input('''Pilih
    1. Untuk Menambahkan Data
    2. Untuk Mengganti Data
    3. Hapus Data
    4. Tampilkan Data
    5. Rata-Rata
    6. Selesai
    7. Urutkan dari yg terbesar
    Masukkan salah satu: '''))

    if pilih == 1:
        nama = input('Nama: ')
        nrp = input('NRP: ')
        nilai = input('Nilai: ')
        baris_baru = []
        baris_baru.append(nrp)
        baris_baru.append(nama)
        baris_baru.append(nilai)
        menu.append(baris_baru)
    elif pilih == 2:
        ganti_list = input('Masukkan Data yang ingin di ganti: ')
        if ganti_list == 'nrp':
            ganti_nrp = input('Masukkan NRP yang ingin di ganti: ')
            for i in menu:
                if i[0] == ganti_nrp:
                    index_nrp = menu.index(i)
                    nrp_baru = input('Masukkan NRP baru: ')
                    menu[index_nrp][0] = nrp_baru
        elif ganti_list == 'nama':
            ganti_nama = input('Masukkan Nama yang ingin di ganti: ')
            for i in menu:
                if i[1] == ganti_nama:
                    index_nama = menu.index(i)
                    nama_baru = input('Masukkan Nama baru: ')
                    menu[index_nama][1] = nama_baru
        elif ganti_list == 'nilai':
            ganti_nilai = int(input('Masukkan Nilai yang ingin di ganti: '))
            for i in menu:
                if i[2] == ganti_nilai:
                    index_nilai = menu.index(i)
                    nilai_baru = int(input('Masukkan Nilai baru: '))
                    menu[index_nilai][2] = nilai_baru
                    break
            else:
                print('Nilai tidak ditemukan')
        else:
            print('Data tidak di temukan')

    elif pilih == 3:
        nrp = input('Masukkan NPR yang ingin di hapus: ')
        for i in menu:
            if i[2] == nrp:
                index_del = menu.index(i)
                menu.pop(index_del)

    elif pilih == 4:
        continue
    elif pilih == 5:
        total = 0
        for i in menu:
            temp = i[2]
            total += temp

        rata_rata = total/len(menu[2])
        print(f'Rata-Rata nilai : {rata_rata:.2f}')
    elif pilih == 6:
        break
    elif pilih == 7:
        n = len(menu)
        for i in range(n):
            swapped = False

            for j in range(n-1-i):
                if menu[j][2] < menu[j+1][2]:
                    menu[j], menu[j+1] = menu[j+1], menu[j]
                    swapped = True
            if not swapped:
                    break


