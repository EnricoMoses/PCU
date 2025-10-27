n = 4
angka = 0
for i in range(1, n+1):
    for j in range(i):
        print(angka % 10, end='')
        angka += 1


    print()