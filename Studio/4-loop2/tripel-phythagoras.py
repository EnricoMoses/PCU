awal = int(input())
akhir = int(input())

ditemukan = False
for a in range(awal, akhir+1):
    for b in range(a+1, akhir+1):
        for c in range(b+1, akhir+1):
            if (a ** 2 + b ** 2) == c ** 2:
                print(a, b, c)
                ditemukan = True

if not ditemukan:
    print('kosong')
