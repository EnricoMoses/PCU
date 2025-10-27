import random

row = int(input('Input row: '))
column = int(input('Input column: '))


mat = []
i = 0
while i < row:
    baris = []
    j = 0
    while j < column:
        baris.append(random.randint(1,10))
        j += 1
    mat.append(baris)
    i += 1

while True:
    print('Matrix: ')
    i = 0
    while i < len(mat):
        j = 0
        while j < len(mat[0]):
            print(mat[i][j], end=' ')
            j += 1
        print()
        i += 1

    print('''1. Rotate Right
2. Rotate Left
3. Flip Horizontal
4. Flip Vertical
5. Exit''')
    pilihan = int(input('Pilihan: '))

    if pilihan == 1:
        baris = len(mat)
        kolom = len(mat[0])
        baru = []
        j = 0
        while j < kolom:
            baris_baru = []
            i = baris - 1
            while i >= 0:
                baris_baru.append(mat[i][j])
                i -= 1
            baru.append(baris_baru)
            j += 1
        mat = baru

    elif pilihan == 2:
        baris = len(mat)
        kolom = len(mat[0])
        baru = []
        j = kolom - 1
        while j >= 0:
            baris_baru = []
            i = 0
            while i < baris:
                baris_baru.append(mat[i][j])
                i += 1
            baru.append(baris_baru)
            j -= 1
        mat = baru

    elif pilihan == 3:
        baris = len(mat)
        kolom = len(mat[0])
        baru = []
        i = 0
        while i < baris:
            baris_baru = []
            j = kolom - 1
            while j >= 0:
                baris_baru.append(mat[i][j])
                j -= 1
            baru.append(baris_baru)
            i += 1
        mat = baru

    elif pilihan == 4:
        baris = len(mat)
        kolom = len(mat[0])
        baru = []
        i = baris - 1
        while i >= 0:
            baris_baru = []
            j = 0
            while j < kolom:
                baris_baru.append(mat[i][j])
                j += 1
            baru.append(baris_baru)
            i -= 1
        mat = baru

    elif pilihan == 5:
        print('Matrix: ')
        i = 0
        while i < len(mat):
            j = 0
            while j < len(mat[0]):
                print(mat[i][j], end=' ')
                j += 1
            print()
            i += 1
        print('Adios...')
        break
    else:
        print('Pilihan tidak valid. Silahkan coba lagi.\n')


