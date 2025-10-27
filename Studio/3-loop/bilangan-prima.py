n = int(input())

# Anggap awalnya prima
is_prima = True

# Bilangan kurang dari 2 bukan prima
if n < 2:
    is_prima = False
else :
    # Cek faktor dari 2 sampai n - 1
    for i in range(2, n):
        if n % i == 0:
            is_prima = False
            break

if is_prima:
    print('PRIMA')
else :
    print('TIDAK PRIMA')