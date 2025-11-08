try:
    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
    daftar = []
    for i in range(jumlah_mahasiswa):
        while True:
            try:
                data = []
                nama = input("Nama: ")
                nilai = int(input("Nilai: "))
                if nilai < 0 or nilai > 100:
                    raise Exception("Nilai harus di antara 0-100")
                data.append(nama)
                data.append(nilai)
                daftar.append(data)
                break
            except ValueError:
                print('Nilai harus berupa angka')
            except Exception as e:
                print('Error: ', e)

except ValueError:
    print('Error: Input harus angka')
else:
    for x in daftar:
        print(x[0], x[1])

