n = int(input())

awal = 0
for i in range(1, n+1):
    # print(i)
    hasil_pangkat = i ** 3
    print(hasil_pangkat)
    jumlah = hasil_pangkat + awal
    awal = jumlah

print(jumlah)
