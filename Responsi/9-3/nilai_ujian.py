nilai = int(input('Masukkan nilai ujian: '))

if nilai >= 85:
    print('A')
elif 70 <= nilai < 85:
    print('B')
elif 55 <= nilai < 70:
    print('C')
else:
    print('D')
