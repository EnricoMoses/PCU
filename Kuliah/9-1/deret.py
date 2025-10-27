while True:
    angka1 = int(input('Masukkan angka 1'))
    angka2 = int(input('Masukkan angka 2'))
    angka3 = int(input('Masukkan angka 3'))

    if angka2 - angka1 == angka3 - angka2:
        print('Merupakan deret aritmatika')
    elif angka2 / angka1 == angka3 / angka2:
        print('Merupakan deret geometri')
    else:
        print('Bukan merupakan deret aritmatika atau geometri')

    lanjut = input('Apakah masih mau lanjut (y/n)')
    if lanjut != 'y':
        break