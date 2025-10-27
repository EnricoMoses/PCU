while True:
    n = int(input('Masukkan jumlah baris (>= 3): '))
    if n >= 3:
        break

prima_awal = 2
for i in range(1, n + 1):
    tercetak = 0
    while tercetak < i:
        if prima_awal >= 2:
            prima = True
            d = 2
            while d * d <= prima_awal:
                if prima_awal % d == 0:
                    prima = False
                    break
                d += 1

            if prima:
                print(prima_awal, end=' ' if tercetak < i - 1 else '')
                tercetak += 1
        prima_awal += 1
    print()

