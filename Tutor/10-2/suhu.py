data =[
    ['p1', 'Adi', 'tinggi', 38.7, 'Pneumonia; Demam Berdarah'],
    ['p2', 'Ani', 'normal', 35.7, 'Penyakit tidak dikenali'],
    ['p1', 'Surya', 'rendah', 37.0, 'Vertigo']
]

while True:
    for i in range(len(data)):
        print(f'ID: {data[i][0]}\tNama: {data[i][1]}\tTD: {data[i][2]}\tSuhu: {data[i][3]}\tDx: {data[i][4]}')
    print('Pilih: ')
    input_s = int(input('1. Tambah 2. Ubah 3. Hapus 4.Tampilkan\n5.Rata-Rata 6.Urutkan 7. Hapus 8. Tampilkan\n '))

    if input_s == 1:
        id_pas = input('Input ID Pasien: ')
        nama = input('Input Nama Pasien: ')
        tekanan_darah = input('Input Tekan Darah: (normal/rendah/tinggi)')
        suhu = float(input('Input Suhu: '))
        gejala = input('Input Gejala (batuk, sesak, nyeri otot): ').split()

        # baris_baru = []
        diagnosis = []
        if 'batuk' in gejala and 'sesak' in gejala and suhu > 37.5 and (tekanan_darah == 'normal' or tekanan_darah == 'tinggi'):
            diagnosis.append('Pneumonia')
        if 'batuk' in gejala and 'sakit_tenggorokan'in gejala and 37.0 <= suhu <= 37.5:
            diagnosis.append('Flu')
        if 'batuk' in gejala and 'nyeri_otot' in gejala and suhu > 38.5:
            diagnosis.append('Demam Berdarah')
        if 'sakit_kepala' and 'mual' and 'pengheliatan_kabur' in gejala:
            diagnosis.append('Migrain')
        if 'sakit_kepala' and 'mual' and 'pusing' in gejala and tekanan_darah == 'rendah':
            diagnosis.append('Vertigo')
        if 'diare' and 'mual' in gejala and 36.0 <= suhu <= 37.5:
            diagnosis.append('Keracunan Makanan')
        if 'diare' and 'demam' in gejala and suhu > 37.5:
            diagnosis.append('Infeksi Usus')

        if diagnosis:
            dx = '; '.join(diagnosis)
        else:
            dx = 'Penyakit tidak ditemukan'
        data.append([id_pas, nama, tekanan_darah, suhu, dx])

    if input_s == 2:
        id_pas = input('Input ID Pasien: ')
        for i in data:
            if i[0] == id_pas:
                idx = data.index(i)
                ubah = input('Input Ubah Data: ')
                if ubah == 'nama':
                    baru = input('Input Nama Baru Data: ')
                    data[i][1] = baru
                elif ubah == 'tekanan_darah':
                    baru = input('Input Tekan Darah Baru Data: ')
                    data[i][2] = baru
                elif ubah == 'suhu':
                    baru = input('Input Suhu Baru Data: ')
                    data[i][3] = baru
                elif ubah == 'gejala':
                    baru = input('Input Gejala Baru Data: ').split('; ')
                    data[i][4] = baru
                else:
                    print('Data tidak di temukan')

                tekanan_darah, suhu, gejala = data[i][2], data[i][3], data[i][4]
                diagnosis = []
                if 'batuk' in gejala and 'sesak' in gejala and suhu > 37.5 and (
                        tekanan_darah == 'normal' or tekanan_darah == 'tinggi'):
                    diagnosis.append('Pneumonia')
                if 'batuk' in gejala and 'sakit_tenggorokan' in gejala and 37.0 <= suhu <= 37.5:
                    diagnosis.append('Flu')
                if 'batuk' in gejala and 'nyeri_otot' in gejala and suhu > 38.5:
                    diagnosis.append('Demam Berdarah')
                if 'sakit_kepala' and 'mual' and 'pengheliatan_kabur' in gejala:
                    diagnosis.append('Migrain')
                if 'sakit_kepala' and 'mual' and 'pusing' in gejala and tekanan_darah == 'rendah':
                    diagnosis.append('Vertigo')
                if 'diare' and 'mual' in gejala and 36.0 <= suhu <= 37.5:
                    diagnosis.append('Keracunan Makanan')
                if 'diare' and 'demam' in gejala and suhu > 37.5:
                    diagnosis.append('Infeksi Usus')

                if diagnosis:
                    dx = '; '.join(diagnosis)
                else:
                    dx = 'Penyakit tidak ditemukan'
                data[i][4] = dx

    elif input_s == 3:
        id_hps = input('Input ID Pasien: ')
        for i in data:
            if i[0] == id_hps:
                idx = data.index(i)
                data.pop(idx)


    elif input_s == 4:
        print('ID\t|Nama\t|TD\t|Suhu\t|Diagnosis')
        continue
    elif input_s == 5:
        total = 0
        for i in data:
            temp = i[3]
            total += temp

        rata_rata = total/len(data)
        print(f'rata-rata: {rata_rata:.2f}')
    # elif input_s == 6:
    # #     toloong bantu bagian ini
    elif input_s == 7:
        break





