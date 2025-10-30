# function untuk input array
def inputArray():
    # user menginput panjang array
    n = int(input('Masukkan panjang array: '))
    # buat array kosong dulu
    arr = []
    # loop sejumlah n kali
    for i in range(1, n+1):
        # user memasukkan isi dari array ke i
        isi = int(input(f'Masukkan elemen ke-{i}: '))
        # append isi ke array kosong tadi
        arr.append(isi)
    # jika sudah return array nya
    return arr

# function untuk cek apakah pola naik atau pola turun
def checkPattern(arr):
    # jika panjang kurang dari 2 atau hanya 1 di anggap naik
    if len(arr) < 2:
        return 'Naik'
    # cek apakah semua isi array lebih kecil dari setelahnya, jika iya return naik
    if all(arr[i] < arr[i+1] for i in range(len(arr)-1)):
        return 'Naik'
    # cek apakah semua isi array lebih besar dari setelahnya jika iya return turun
    if all(arr[i] > arr[i+1] for i in range(len(arr)-1)):
        return 'Turun'
    # jika tidak memenuhi kedua kondisi tersebut artinya listnya campuran
    return 'Campuran'

# cek ada berapa segmen yang naik dan ada berapa segmen yang turun
# segmen adalah bagian dari list itu sendiri
def countSegment(arr):
    # buat variabel awal naik, turun = 0
    naik = 0
    turun = 0

    # jika panjang list kurang dari 2 maka tidak ada segmen
    if len(arr) < 2:
        # langsung return 0, 0
        return naik, turun

    # buat variabel arah untuk menentukan arah
    # misal 1 -> segmen naik
    # -1 -> segmen turun
    # 0 -> putus karena menemukan isi yg sama
    # buat terlebih dahulu arahnya 0
    arah = 0

    # loop sesuai jumlah array
    for i in range(1, len(arr)):
        # jika elemen saat ini lebih besar dari elemen sebelumnya
        if arr[i] > arr[i-1]:
            # agar tidak menabrak dengan segmennya sendiri
            if arah != 1:
                # tambahkan naik +1
                naik += 1
                # arah kita jadikan 1 karena naik
                arah = 1
        #  jika elemen saat ini lebih kecil dari elemen sebelumnya
        elif arr[i] < arr[i-1]:
            # agar tidak menabrak dengan segmennya sendiri
            if arah != -1:
                # tambahkan turun +1
                turun += 1
                # arah jadikan -1 karena turun
                arah = -1
        else:
            # kondisi ketika elemen sama dengan elemen sebelumnya
            # reset arah menjadi 0
            arah = 0
    # lalu returnkan jumlah naik, turun nya
    return naik, turun

# Main
# =============================
array = inputArray()
print('Array: ', array)

pola = checkPattern(array)
naik, turun = countSegment(array)

print(f'Pola array: {pola}')
print(f'Jumlah segmen naik: {naik}')
print(f'Jumlah segmen turun: {turun}')