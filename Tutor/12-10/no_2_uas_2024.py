from itertools import combinations

def baca_layanan():
    n = int(input())

    layanan = []

    for i in range(n):
        data = input().split()
        nama = data[0]
        durasi = float(data[1])
        biaya = int(data[2])
        layanan.append([nama, durasi, biaya])

    return layanan

def pilih_layanan(layanan, maks_duration):
    best_comb = []
    min_biaya = float('inf')
    jumlah_terbanyak = 0
    n = len(layanan)

    for i in range(1, n + 1):
        for comb in combinations(layanan, i):
            total_jam = sum(x[1] for x in comb)
            total_biaya = sum(x[2] for x in comb)

            if total_jam <= maks_duration:
                if (i > jumlah_terbanyak) or \
                        (i == jumlah_terbanyak and total_biaya < min_biaya):
                    jumlah_terbanyak = i
                    min_biaya = total_biaya
                    best_comb = comb

    return best_comb, jumlah_terbanyak, min_biaya

def cetak_hasil(kombinasi, jumlah, biaya):
    if not kombinasi:
        print('Tidak ada layanan yang dapat dikerjakan')
        return

    daftar_nama = [nama for (nama, durasi, b) in kombinasi]

    # gabungkan jadi satu string dipisah koma
    nama_gabungan = ", ".join(daftar_nama)

    # cetak satu baris saja
    print(nama_gabungan)
    print(f"<bisa mengerjakan {jumlah} layanan dengan total biaya {biaya}>")


def main():
    # total jam kerja: 8–16 dikurangi 1 jam istirahat = 7 jam
    maks_duration = 7.0

    # layanan = baca_layanan()
    layanan = [
        ["Adi", 1.5, 12],
        ["Budi", 1, 10],
        ["C", 3, 30],
        ["D", 5.5, 30],
        ["E", 4, 15],
        ["F", 4.5, 20],
        ["G", 3.5, 10],
    ]
    kombinasi, jumlah, biaya = pilih_layanan(layanan, maks_duration)
    cetak_hasil(kombinasi, jumlah, biaya)

main()