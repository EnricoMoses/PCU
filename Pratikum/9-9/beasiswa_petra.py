ipk = float(input('Masukkan IPK: '))
sks = int(input('Masukkan SKS: '))
absen = int(input('Masukkan absen: '))
is_D_E = str(input('Ada nilai D/E (ya/tidak): '))

if ipk >= 3.5:
    if absen <= 3:
        if is_D_E == 'ya':
            print('Tidak Lulus (Nilai Buruk)')
        else :
            print('Lulus Beasiswa Penuh')
    elif 4 <= absen <= 5:
        if is_D_E == 'ya':
            print('Tidak Lulus (Nilai Buruk)')
        else :
            print('Lulus Beasiswa Parsial')
    else :
        print('Tidak Lulus (Absensi)')
elif 3.0 <= ipk < 3.5:
    if sks >= 20 and absen <= 5:
        if is_D_E == 'ya':
            print('Tidak Lulus (Nilai Buruk)')
        else :
            print('Lulus Beasiswa Parsial')
    else :
        print('Tidak Lulus')
else:
    print('Tidak Lulus (IPK)')