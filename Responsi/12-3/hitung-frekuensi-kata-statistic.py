def hitung_statistic(teks):
    if teks is None or not isinstance(teks, str) or len(teks) == 0:
        raise ValueError('Input harus berupa teks dan tidak boleh kosong')

    kata_list = teks.split()

    total_kata = len(kata_list)

    frekuensi = {}
    for kata in kata_list:
        if kata in frekuensi:
            frekuensi[kata] += 1
        else:
            frekuensi[kata] = 1

    kata_unik = len(frekuensi)


    # cari kata yang paling sering muncul
    kata_tersering = None
    jumlah_tersering = 0
    for k, v in frekuensi.items():
        if v > jumlah_tersering:
            kata_tersering = k
            jumlah_tersering = v

    return {
        'total_kata': total_kata,
        'kata_unik': kata_unik,
        'kata_tersering': (kata_tersering, jumlah_tersering),
    }

teks = "Saya suka belajar Python karena Python sangat seru dan Python itu powerful."

try :
    hasil = hitung_statistic(teks)
except ValueError as e:
    print(e)
    hasil = {}

print(hasil)