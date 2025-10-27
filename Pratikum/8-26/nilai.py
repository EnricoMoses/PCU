nilai1 = float(input('Nilai 1: '))
nilai2 = float(input('Nilai 2: '))
nilai3 = float(input('Nilai 3: '))

if (0 <= nilai1 <= 100) and (0 <= nilai2 <= 100) and (0 <= nilai3 <= 100):
    rata_rata = (nilai1 + nilai2 + nilai3) / 3
    print(f'Rata Rata: {rata_rata}')
else :
    print('Nilai tidak masuk akal')