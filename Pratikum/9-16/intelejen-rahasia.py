stream = input().strip()
x = int(input().strip())

vokal = 'AIUEO'
kode = ''
i = 0
while i < len(stream):
    ch = stream[i].upper()

    if 'A' <= ch <= 'Z':
        if ch == 'X':
            break
        if ch in vokal:
            i += 1
            continue

        kode += ch
        if len(kode) == 7:
            break

    i += 1

print(f'Kode Rahasia: {kode}')

enkripsi = ''
j = 0
while j < len(kode):
    ascii_baru = ord(kode[j]) + x
    ch_baru = chr(ascii_baru)
    if 'A' <= ch_baru <= 'Z':
        enkripsi += ch_baru
    j += 1
print(f'Enkripsi: {enkripsi}')