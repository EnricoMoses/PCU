from math import dist

class OutOfAreaError(Exception):
    pass

def covert_to_tuple(input_str):
    try:
        parts = input_str.split(',')
        if len(parts) != 2:
            raise ValueError
        x = int(parts[0])
        y = int(parts[1])
        return (x,y)
    except:
        raise ValueError

def check_value(kordinat):
    x, y = kordinat
    if x < -100 or x > 100 or y < -100 or y > 100:
        raise OutOfAreaError('Koordinat di luar area operasi')

def kirim_drone(list_target, nomor_target):
    target = list_target[nomor_target - 1]
    jarak = dist((0,0), target)
    print(f'Drone dikirim ke koordinat {target} dengan jarak ke target sejauh {jarak:.2f} km')

while True:
    try:
        jumlah = int(input('Input jumlah target: '))
        if jumlah < 0:
            raise ValueError
        break
    except ValueError:
        print('Jumlah target tidak valid')

targets = []
i = 1
while i <= jumlah:
    try:
        inp = input(f'Input koordinat {i}: ')
        koord = covert_to_tuple(inp)
        check_value(koord)
        targets.append(koord)
        i += 1
    except ValueError:
        print('Koordinat salah')
    except OutOfAreaError as e:
        print(e)

print(f'Daftar Target: {targets}')

while True:
    try:
        nomor = int(input('Input target operasi: '))
        if nomor == 0:
            print('Operasi selesai')
            break
        if nomor < 0:
            raise ValueError
        if nomor > len(targets):
            raise IndexError

        kirim_drone(targets, nomor)

    except ValueError:
        print('Target tidak valid')
    except IndexError:
        print('Target tidak ada')

