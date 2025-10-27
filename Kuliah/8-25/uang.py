uang = int(input('Masukkan Uang Maks dalam Juta : '))

jutaan = uang // 1_000_000
ratusan_ribu = uang // 100_000 % 10
puluhan_ribu = uang // 10_000 % 10
ribuan = uang // 1_000 % 10
ratusan = uang // 100 % 10
puluhan = uang // 10 % 10
satuan = uang % 10

if jutaan != 0:
    print(jutaan, 'x juta')
if ratusan_ribu != 0:
    print(ratusan_ribu, 'x ratusan ribu')
if puluhan_ribu != 0:
    print(puluhan_ribu, 'x puluhan ribu')
if ribuan != 0:
    print(ribuan, 'x ribuan')
if ratusan != 0:
    print(ratusan, 'x ratusan')
if puluhan != 0:
    print(puluhan, 'x puluhan')
if satuan != 0:
    print(satuan, 'x satuan')

'''
CT:

Dekomposisi:
Masalah dipecah menjadi tugas yang lebih kecil-kecil
    1. Input: berupa angka integer (total jumlah uang, maksimal dalam jutaan)
    2. Kalkulasi Jutaan : Menghitung kelipatan jutaan dari total uang
    3. Kalkulasi Ratusan Ribu: Menghitung angka pada posisi ratusan ribu
    4. Kalkulasi Puluhan Ribu: Menghitung angka pada posisi puluhan ribu
    5. Kalkulasi Ribuan: Menghitung angka pada posisi ribuan
    6. Kalkulasi Ratusan: Menghitung angka pada posisi ratusan
    7. Kalkulasi Puluhan: Menghitung angka pada posisi puluhan
    8. Kalkulasi Satuan: Menghitung angka pada posisi satuan
    Output: Menampilkan setiap hasil perhitungan yang nilainya tidak nol
    
Pattern Recognition
    - Pola perhitungan digit: Untuk mendapatkan angka di setiap posisi, menggunakan
    pola yang sama
    - Pola pengecekan kondisi : Untuk menampilkan hasil yang bukan nol, menggukakan
    pengecekan berulang, jika nilai 0 maka tidak akan ditampilkan
    
Abstraksi
    - Fokus pada nilai numerik uangnya. Tidak peduli uang dalam fisik (kertas atau
    logam) atau transfer digital
    - Penggunaan nama variabel yang deskriptif, mewakili sebuah nilai pada posisi 
    tertentu 
    - Nilai tempat (ratusan, puluhan, satuan) digunakaan untuk menyederhanakan 
    untuk memahami angka
    
Algoritma
    1. Mulai
    2. Menginputkan angka yaitu total uang, Maksimal jutaan
    3. Menyimpan angka tersebut ke dalam varibel uang
    4. Menghitung jutaan dengan membagi dengan 1.000.000 menggunakan pembagian
    integer (//)
    5. Menghitung ratusan_ribu dengan membagi dengan 100.000 menggunakan pembagian
    integer (//), lalu ambil sisa baginya dengan modulo (%) dengan 10
    6. Mengulangi 5 langkah untuk puluhan_ribu, ribuan, ratusan, puluhan, dan satuan
    dengan nilai pembagi yang sesuai
    7. Memeriksa apakah jutaan dan hasil lainnya tidak sama dengan 0. Jika ya, 
    menampilkan nilainya
    8. Selesai 

'''