detik = int(input("Masukkan detik: "))
format = input('Masukkan format (jam, menit, detik): ')

if format == 'jam':
    print(f'{detik / 3600} Jam')
elif format == 'menit':
    print(f'{detik / 60} Menit')
elif format == 'detik' :
    print(f'{detik} Detik')
else :
    print('Anda salah memasukkan format')

# print(f'{detik // 3600} Jam {detik % 3600 // 60} Menit {detik % 60} Detik')



