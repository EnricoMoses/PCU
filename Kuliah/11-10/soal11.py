data = [
    ("Andi", {"algoritma": 85, "struktur data": 78, "basis data": 90}),
    ("Budi", {"algoritma": 75, "struktur data": 82, "basis data": 70}),
    ("Citra", {"algoritma": 92, "struktur data": 88, "basis data": 95})
]

rata_nilai = {}

for nama, mata_kuliah in data:
    total = sum(mata_kuliah.values())
    jumlah_mk = len(mata_kuliah)
    rata = total / jumlah_mk
    rata_nilai[nama] = rata

    print(f'{nama}: {rata:.2f}')

print('\nrata-rata=', rata_nilai)

mahasiswa_terbaik = max(rata_nilai, key=rata_nilai.get)
print(mahasiswa_terbaik)