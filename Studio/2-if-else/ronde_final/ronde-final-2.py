# Kompetisi Solute - Basha Bashi (perbaikan: pakai selisih per ronde)
# Urutan input per ronde: Ron (Ri) lalu Neil (Ni), sesuai contoh test case.

x = int(input())

if x <= 0:
    print("Tidak valid!")
else:
    max_selisih = 0
    pemenang = ""

    ronde = 1
    while ronde <= x:
        r = int(input())  # skor Ron de Fin AI
        n = int(input())  # skor Neil AI

        if r > n:
            selisih = r - n
            if selisih > max_selisih:
                max_selisih = selisih
                pemenang = "Ron de Fin AI"
        elif n > r:
            selisih = n - r
            if selisih > max_selisih:
                max_selisih = selisih
                pemenang = "Neil AI"
        # jika r == n, tidak mengubah max_selisih (tie ronde ini)
        ronde += 1

    # Jika semua ronde seri (max_selisih == 0), tambah ronde sampai ada pemenang
    while max_selisih == 0:
        r = int(input())
        n = int(input())
        if r > n:
            max_selisih = r - n
            pemenang = "Ron de Fin AI"
        elif n > r:
            max_selisih = n - r
            pemenang = "Neil AI"
        # kalau masih seri, lanjut baca lagi

    print(pemenang, "unggul dengan nilai", max_selisih)
