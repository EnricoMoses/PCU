nama = input('Input nama: ')
tahun_lahir = input('Input tahun lahir: ')
alamat = input('Input Alamat: ')
nilai_semester1 = float(input('Nilai semester 1: '))
nilai_semester2 = float(input('Nilai semester 2: '))
nilai_semester3 = float(input('Nilai semester 3: '))
nilai_semester4 = float(input('Nilai semester 4: '))

rata_rata = (nilai_semester1 + nilai_semester2 + nilai_semester3 + nilai_semester4) / 4

print('=== DATA MAHASISWA ===')
print(f'Nama        : {nama}')
print(f'Tahun lahir : {tahun_lahir}')
print(f'Alamat      : {alamat}')
print(f'Rata-rata Nilai Semester 1-4: {rata_rata:.1f}')