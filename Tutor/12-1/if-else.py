# angka = int(input('Masukkan angka: '))
#
# if angka > 0:
#     print('Angka Positif')
#
# if angka < 0:
#     print('Angka Negatif')
#
# if angka == 0:
#     print('Angka nol')

# nilai = int(input('Masukkan nilai : '))
#
# if nilai >= 60:
#     print('Anda lulus')
# else:
#     print('Anda tidak lulus')

# nilai = int(input('Masukkan nilai: '))
#
# if nilai >= 90:
#     print('Grade A')
# elif nilai >= 80:
#     print('Grade B')
# elif nilai >= 70:
#     print('Grade C')
# elif nilai >= 60:
#     print('Grade D')
# else:
#     print('Grade E')

umur = int(input('Umur: '))
punya_sim = input('Punya Sim (ya/tidak): ')

if umur >= 17 or punya_sim == 'ya':
    print('Boleh mengendarai motor')
else:
    print('Tidak boleh mengendarai motor')