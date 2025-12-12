def input_nilai():
    data = {}
    while True:
        nama = input('Masukkan nama (stop selesai): ')
        if nama == 'stop':
            break
        if nama == '':
            print('Nama tidak boleh kosong')
            continue

        while True:
            nilai = input(f'masukkan nilai {nama}: ')
            try:
                nilai = float(nilai)
            except ValueError:
                print('Nilai harus berupa angka!')
                continue

            if 0 <= nilai <= 100:
                data[nama] = nilai
                break
            else:
                print('Nilai harus 0-100')
    return data

def rangkuman_data(data):
    kategori = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
    }

    if not data:
        return (None, None, None, kategori)

    nilai_list = list(data.values())
    nilai_tertinggi = max(nilai_list)
    nilai_terendah = min(nilai_list)
    rata_rata = sum(nilai_list) / len(nilai_list)

    for nilai in nilai_list:
        if nilai >= 85:
            kategori['A'] += 1
        elif nilai >= 75:
            kategori['B'] += 1
        elif nilai >= 65:
            kategori['C'] += 1
        elif nilai >= 50:
            kategori['D'] += 1
        else:
            kategori['E'] += 1

    return (nilai_tertinggi, nilai_terendah, rata_rata, kategori)



data = input_nilai()
maks, mins, avg, kategori = rangkuman_data(data)

print('\n--- Daftar Nilai ---')
if not data:
    print('Tidak ada data')
else:
    for nama, nilai in data.items():
        tampil = int(nilai) if float(nilai).is_integer() else nilai
        print(f'Nilai {nama}: {tampil}')

print('\n--- Rangkuman Nilai ---')
if not data:
    print('Nilai tertinggi  : -')
    print('Nilai terendah   : -')
    print('Rata-rata        : -')
else:
    print(f'Nilai tertinggi : {maks:g}')
    print(f'Nilai terendah  : {mins:g}')
    print(f'Rata-rata       : {avg:.2f}')

print('Kategori:')
for k in ['A', 'B', 'C', 'D', 'E']:
    print(f'{k}: {kategori[k]}')