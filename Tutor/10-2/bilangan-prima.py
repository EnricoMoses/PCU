angka = [1,2,3,4,5,6,7,8,9]

prima = []
for i in angka:
    isPrima = True
    if i < 2:
        isPrima = False
    else:
        for j in range(2, i):
            if i % j == 0:
                isPrima = False

    if isPrima:
        prima.append(i)

print(prima)