# for i in range(5,10):
#     print(i)
#     print(15-i)

# print(False and True or True)

tinggi = 4

# Perulangan untuk setiap baris
for i in range(1, tinggi + 1):
    # Cetak spasi di sisi kiri (sama seperti sebelumnya)
    print(" " * (tinggi - i), end="")
    # print(i)

    # Kondisi untuk mencetak bintang atau spasi
    # Jika ini adalah baris pertama atau baris terakhir
    if i == 1 or i == tinggi:
        print("*" * (2 * i - 1))
    # Jika ini adalah baris-baris di tengah
    else:
        # Cetak bintang kiri
        print("*", end="")
        # Cetak spasi di bagian dalam
        print(" " * (2 * i - 3), end="")
        # Cetak bintang kanan
        print("*")