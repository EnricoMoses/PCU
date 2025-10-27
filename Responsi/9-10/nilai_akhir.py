skor = int(input())

grade = ''
keterangan = ''
if skor >= 85:
    grade = 'A'
    if skor >= 95:
        keterangan = 'Sangat Istimewa'
    else:
        keterangan = 'Baik Sekali'
elif 70 <= skor < 85:
    grade = 'B'
    if skor >= 80:
        keterangan = 'Baik'
    else:
        keterangan = 'Cukup Baik'
elif 55 <= skor < 70:
    grade = 'C'
    if skor >= 65:
        keterangan = 'Cukup'
    else:
        keterangan = 'Kurang'
else:
    grade = 'D'
    keterangan = 'Tidak Lulus'

print(f'Grade: {grade}')
print(f'Keterangan: {keterangan}')