stok = {
    'apel': 5,
    'jeruk': 2,
    'mangga': 10
}

buah = input('Masukkan nama buah: ')
if buah in stok:
    print(stok[buah])
else:
    print('Buah tidak di temukan')
