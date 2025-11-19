from mathops.basic import tambah, kurang

def input_float(prompt):
    while True:
        try:
            nilai = float(input(prompt))
            return nilai
        except ValueError:
            print('Input tidak valid. Masukkan angka lagi')

def cetak_hasil(label, nilai):
    if isinstance(nilai, float) and nilai.is_integer():
        print(f'{label}: {int(nilai)}')
    else:
        print(f'{label}: {nilai}')

a = input_float('Masukkan angka 1: ')
b = input_float('Masukkan angka 2: ')

hasil_tambah = tambah(a, b)
hasil_kurang = kurang(a, b)

cetak_hasil('Hasil tambah', hasil_tambah)
cetak_hasil('Hasil kurang', hasil_kurang)