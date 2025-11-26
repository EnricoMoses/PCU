def substring_terpanjang(kata):
    if not kata:
        return 0

    terpendek = min(kata, key=len)
    n = len(terpendek)

    for panjang in range(n, 0, -1):
        for start in range(0, n - panjang + 1):
            sub = terpendek[start:start+panjang]

            if all(sub in k for k in kata):
                return sub
    return ''

jumlah = int(input('Masukkan jumlah string: '))
strings = []

for i in range(jumlah):
    s = input(f'Masukkan string ke-{i+1}: ')
    strings.append(s)

hasil = substring_terpanjang(strings)

print(hasil)