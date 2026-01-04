from itertools import combinations


def judul_bersih_list(str):
    s = str.lower().replace('.', '').replace(',', '').split()

    unik = []
    for i in s:
        if i not in unik:
            unik.append(i)
    return unik

def hitung_kemiripan(j1, j2):
    w1 = judul_bersih_list(j1)
    w2 = judul_bersih_list(j2)

    if len(w1) == 0 and len(w2) == 0:
        return 0

    sama = 0
    for kata in w1:
        if kata in w2:
            sama += 1

    terbanyak = max(len(w1), len(w2))

    return (sama / terbanyak) * 100

def cari_semua_kemiripan(daftar):
    hasil = []
    for j1, j2 in combinations(daftar, 2):
        persen = hitung_kemiripan(j1, j2)
        hasil.append([persen, j1, j2])
    return hasil

def tampil_kemiripan(daftar_kemiripan):
    for persen, j1, j2 in daftar_kemiripan:
        print(f'[{persen:.1f}%]')
        print(j1)
        print('<-->')
        print(j2)
        print()

def tampil_palning_mirip(daftar_kemiripan):
    if not daftar_kemiripan:
        print('Tidak ada judul paling mirip')
        return

    maks = max(daftar_kemiripan, key=lambda x:x[0])
    if maks[0] == 0:
        print('Tidak ada judul paling mirip')
        return

    persen, j1, j2 = maks
    print('===== Judul paling mirip =====')
    print(f'[{persen:.1f}%]')
    print(j1)
    print('<-->')
    print(j2)



n = int(input('Masukkan jumlah judul: '))
daftar = []
for i in range(n):
    judul = input().strip()
    daftar.append(judul)

# print(daftar)
daftar_kemiripan = cari_semua_kemiripan(daftar)
tampil_kemiripan(daftar_kemiripan)
tampil_palning_mirip(daftar_kemiripan)
