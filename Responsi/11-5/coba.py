def rata_rata_nilai():
    # Input satu baris; boleh pakai spasi atau koma sebagai pemisah
    teks = input("Masukkan daftar nilai (pisah dengan spasi atau koma):\n")

    # Ganti koma jadi spasi, lalu split berdasarkan spasi (whitespace)
    tokens = teks.replace(',', ' ').split()

    total = 0.0
    hitung = 0

    for tok in tokens:
        # Bersihkan kutip jika user mengetik 'A' (tetap tanpa regex)
        bersih = tok.strip().strip("'\"")

        try:
            nilai = float(bersih)
        except ValueError:
            print(f"Error: '{bersih}' bukan angka yang valid.")
            continue

        if nilai < 0:
            tampil = int(nilai) if nilai.is_integer() else nilai
            print(f"Error: Nilai {tampil} tidak boleh negatif.")
            continue

        if nilai > 100:
            tampil = int(nilai) if nilai.is_integer() else nilai
            print(f"Error: Nilai {tampil} tidak boleh lebih dari 100.")
            continue

        total += nilai
        hitung += 1

    if hitung > 0:
        print(f"Rata-rata nilai valid: {total / hitung:.2f}")
    else:
        print("Tidak ada nilai valid.")


rata_rata_nilai()