x = int(input())

while x <= 0:
    print('Tidak valid')
else :
    max_selisih = 0
    pemenang = ''

    ronde = 1
    while ronde <= x:
        r = int(input())
        n = int(input())

        if r > n:
            selisih = r - n
            if selisih > max_selisih:
                max_selisih = selisih
                pemenang = "Ron de Fin AI"
        elif n > r:
            selisih = n - r
            if selisih > max_selisih:
                max_selisih = selisih
                pemenang = 'Neil AI'
        ronde = ronde + 1

    while max_selisih == 0:
        r = int(input())
        n = int(input())

        if r > n:
            max_selisih = r - n
            pemenang = 'Ron de Fin AI'
        elif n > r:
            max_selisih = n - r
            pemenang = 'Neil AI'

    print(f'{pemenang} unggul dengan selisih {max_selisih}')