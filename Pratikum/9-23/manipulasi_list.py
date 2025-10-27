import random

n = int(input('Masukkan panjang list (n): '))
data = []
for _ in range(n):
    data.append(random.randint(0, 9))

print(f'Isi list: {data}')

while True:
    print('''==== MENU ====
1. Tampilkan list
2. Reverse (a, b)
3. Rotate kanan (k)
4. Sort list
0. Keluar''')
    pilih = int(input('Pilih menu: '))

    if pilih == 1:
        print(f'Isi list: {data}')
    elif pilih == 2:
        a = int(input('Masukkan a: '))
        b = int(input('Masukkan b: '))
        if a < 1 or b < 1 or a >= b or a > len(data) or b > len(data):
            print('Operasi reverse tidak valid')
        else:
            i = a - 1
            j = b - 1
            while i < j:
                tmp = data[i]
                data[i] = data[j]
                data[j] = tmp
                i += 1
                j -= 1
            print(f'list berhasil di-reverse dari index {a} sampai {b}!')
            print(f'list: {data}')

    elif pilih == 3:
        k = int(input('Masukkan k: '))
        nlen = len(data)
        if nlen > 0:
            k = k % nlen
            for _ in range(k):
                last = data[nlen - 1]
                i = nlen - 1
                while i > 0:
                    data[i] = data[i - 1]
                    i -= 1
                data[0] = last
            print(f'list berhasil di-rotate ke kanan sebanyak {k} langkah!')
            print(f'list: {data}')

    elif pilih == 4:
        print('''Pilih metode sort:
1. Ascending
2. Descending''')
        sub = int(input('Masukkan: '))
        if sub == 1 or sub == 2:
            ascending = (sub == 1)
            nlen = len(data)
            i = 0
            while i < nlen - 1:
                swapped = False
                j = 0
                while j < nlen - 1 - i:
                    if (ascending and data[j] > data[j + 1]) or ((not ascending) and data[j] < data[j + 1]):
                        data[j], data[j + 1] = data[j + 1], data[j]
                        swapped = True
                    j += 1
                if not swapped:
                    break
                i += 1
            print('list berhasil di-sort ascending!' if ascending else 'list berhasil di-sort descending!')
            print(f'list: {data}')
        else:
            print('Pilihan sub-menu tidak valid')
    elif pilih == 0:
        print('Program selesai. Terima kasih!')
        break
    else:
        print('Pilihan menu tidak valid')


