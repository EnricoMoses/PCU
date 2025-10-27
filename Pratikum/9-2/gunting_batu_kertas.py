import random

pilihan_player = int(input('''
PERMAINAN GUNTING BATU KERTAS
1. Gunting
2. Batu
3. Kertas
CHOICE [1/2/3]:
'''))

if pilihan_player == 1:
    player = 'GUNTING'
elif pilihan_player == 2:
    player = 'BATU'
elif pilihan_player == 3:
    player = 'KERTAS'
else :
    print('Anda salah memasukkan input')
    exit()

pilihan_komputer = random.randint(1,3)

if pilihan_komputer == 1:
    komputer = 'GUNTING'
elif pilihan_komputer == 2:
    komputer = 'BATU'
else :
    komputer = 'KERTAS'

print(f'{player} vs {komputer}')

if player == komputer:
    print('Hasil: Seri')
elif (player == 'BATU' and komputer == 'GUNTING') or \
    (player == 'GUNTING' and komputer == 'KERTAS') or \
    (player == 'KERTAS' and komputer == 'BATU'):
    print('Hasil: Menang')
else:
    print('Hasil: Kalah')



