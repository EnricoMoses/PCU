nilai = int(input('Nilai: '))

if 86 <= nilai <= 100:
    print('A')
elif nilai >= 76:
    print('B+')
elif nilai >= 69:
    print('B')
elif nilai >= 61:
    print('C+')
elif nilai >= 56:
    print('C')
elif nilai >= 41:
    print('D')
elif nilai >= 0:
    print('E')
else:
    print('T')