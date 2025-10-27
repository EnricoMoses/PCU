angka = [5, 12, 19, 24, 35, 40, 57, 68, 72]

hasil = []

for i in angka:
    if i % 2 == 0 and i > 20:
        hasil.append(i)

for i in hasil:
    print(i, end= ' ')