jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

data = []
for i in range(1, jumlah_mahasiswa + 1):
    temp = []
    nama = input(f"Masukkan nama mahasiswa ke-{i}: ")
    temp.append(nama)
    nilai = int(input(f"Masukkan nilai kembali ke-{i}: "))
    temp.append(nilai)
    data.append(temp)

print('Daftar mahasiswa (sebelum data diurutkan)')
for i in range(len(data)):
    print(f'{i+1}. Nama: {data[i][0]}, \t\t Nilai: {data[i][1]}')

nilai_dicari = int(input("Masukkan nilai yang ingin dicari: "))
print(f'Mahasiswa dengan nilai {nilai_dicari}:')

lulus = 0
ga_lulus = 0
for i in data:
    if i[1] == nilai_dicari:
        print(f'Nama: {i[0]}, \t\t Nilai: {i[1]}')
    if i[1] < 60:
        ga_lulus += 1
    else:
        lulus += 1

for i in range(len(data) - 1):
    for j in range(len(data) - i - 1):
        if data[j][1] < data[j + 1][1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print('3 Mahasiswa dengan nilai tertinggi:')
for i in range(3):
    print(f'Nama: {data[i][0]}, \t\t Nilai: {data[i][1]}')


print(f'Jumlah mahasiswa lulus: {lulus} ({(lulus/len(data)*100)}%)')
print(f'Jumlah mahasiswa tidak lulus: {ga_lulus} ({(ga_lulus/len(data)*100)}%)')

print('Daftar mahasiswa (setelah diurutkan berdasarkan nilai):')
for i in range(len(data)):
    print(f'{i+1}. Nama: {data[i][0]}, \t\t Nilai: {data[i][1]}')
