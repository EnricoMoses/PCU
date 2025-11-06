# buat variabel awal total = 0
total = 0
# blok try digunakan agar blok finally bisa dijalankan sesuai yg di minta oleh soal
try:
    # buat while loop utk menerima input berulang2
    while True:
        # suruh user memasukkan harga/selesai
        harga = input("Masukkan harga barang (atau ketik 'selesai'): ")
        # jika user menginput selesai hentikan program
        if harga == 'selesai':
            break
        # taruh kode yg berpotensi error di bawah ini, jika konvert ke int gagal
        try:
            # ubah harga dr string menjadi int, jika error lgsg ke expect
            harga = int(harga)
            # jika harga < 0
            if harga < 0:
                # tampilkan bahwa harga tdk bole negatif, lalu continue ke input selanjutnya
                print('Error: harga tidak boleh negatif')
                continue
            # tambahkan harga ke total utk di tampilkan saat program selesai
            total += harga
        # jika user memasukkan bukan angka dan juga bukan 'selesai'
        except ValueError:
            # tampilkan pesan errornya
            print('Error: input harus berupa angka!')
    # tampilkan total jika user sudah menginputkan selesai
    print(f'Total harga semua barang: {total}')
# jalankan kode finally transaksi selesai sessuai yg di minta oleh soal
# walaupun terjadi error akan tetap di eksekusi kodenya
finally:
    print('Transaksi selesai.')