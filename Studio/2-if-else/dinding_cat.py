bentuk_ruangan = input()

if bentuk_ruangan == 'Kubus':
    for i in range(3):
        sisi = int(input())

    luas_dinding = 4 * sisi * sisi

elif bentuk_ruangan == 'Balok':
    panjang = int(input())
    lebar = int(input())
    tinggi = int(input())

    luas_dinding = 2 * (panjang * tinggi) + 2 * (lebar * tinggi)
elif bentuk_ruangan == 'L':
    panjang_1 = int(input())
    lebar_1 = int(input())
    tinggi_1 = int(input())
    panjang_2 = int(input())
    lebar_2 = int(input())
    tinggi_2 = int(input())

    luas_dinding = (2 * panjang_1 * tinggi_1) + (2 * (panjang_2 + lebar_1) * tinggi_1)

else :
    print('Bentuk ruangan tidak valid')
    exit()

jumlah_kaleng = luas_dinding / 10

if jumlah_kaleng > int(jumlah_kaleng):
    jumlah_kaleng = int(jumlah_kaleng) + 1
else :
    jumlah_kaleng = int(jumlah_kaleng)

print(jumlah_kaleng)
