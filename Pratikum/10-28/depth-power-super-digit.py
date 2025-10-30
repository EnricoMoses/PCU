# function untuk menjumlahkan digit dari angka
def sum_digit(n):
    # return penjumlahan dari setiap digit, diubah ke str dulu lalu
    # hasilnya ubah ke int lagi
    return sum(int(digit) for digit in str(n))

# function untuk memperhitungkan tingkat kedalaman
def depth_power_superdigit(n, depth = 1):
    # jumlahkan digit terlebih dahulu
    s = sum_digit(n)

    # pangkatkan s dengan jumlah kedalaman saat ini
    m = s ** depth

    # jika hasilnya sudah 1 digit maka hasilnya adalah bilangan itu sendiri
    if m < 10:
        return m

    # jika belum lanjut ke ke dalaman berikutnya dengan rekursi func
    return depth_power_superdigit(m, depth + 1)

# untuk menguji functionnya
input_angka = int(input())
print(depth_power_superdigit(input_angka))

