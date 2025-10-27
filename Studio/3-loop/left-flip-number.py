n = str(12345)
x = 2

hasil = []
while n:
    blok = n[-x:]
    n = n[:-x]
    hasil.append(blok)

print(''.join(hasil))

