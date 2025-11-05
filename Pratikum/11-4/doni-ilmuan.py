def minta_hari():
    try :
        n = int(input('Masukkan hari: '))
        if n < 1:
            print('Error: Hari minimal harus 1!')
            return minta_hari()
        return n
    except ValueError:
        print('Error: Input harus berupa angka! Silakan coba lagi.')
        return minta_hari()

def langkah_berikutnya(state):
    t, p, j, r = state
    # hari berikutnya
    t2 = r
    p2 = t
    j2 = p
    r2 = r + j

    return [t2, p2, j2, r2]

def format_barisan(state):
    t, p, j, r = state
    bagian = []
    if r:
        bagian.append(f'{r} raja')
    if j:
        bagian.append(f'{j} jendral')
    if p:
        bagian.append(f'{p} prajurit')
    if t:
        bagian.append(f'{t} tunas')
    return ' '.join(bagian)

def print_perkembangan(target_hari, hari_ke = 1, state = [1, 0, 0, 0]):
    print(f'Hari ke-{hari_ke}: {format_barisan(state)}')
    if hari_ke == target_hari:
        return
    print_perkembangan(target_hari, hari_ke + 1, langkah_berikutnya(state))


x = minta_hari()
print_perkembangan(x)