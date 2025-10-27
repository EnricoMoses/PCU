import random

angka_rahasia = random.randint(1,20)
for i in range(5):
    tebakan = int(input('Tebak angka (1-20): '))
    if tebakan == angka_rahasia:
        print('Selamat, tebakanmu benar!')
        break
    elif  tebakan > angka_rahasia:
        print('Terlalu besar')
    elif tebakan < angka_rahasia:
        print('Terlalu kecil')
else:
    print(f'Kesempatan habis, angka yang benar adalah {angka_rahasia}')