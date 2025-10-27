awal = int(input())
akhir = int(input())

ada = False

for i in range(awal, akhir+1):
    is_prima = True
    if i < 2:
        is_prima = False
    else:
        for j in range(2, i):
            if i % j == 0:
                is_prima = False
                break

    if is_prima:
        print(i, end=" ")
        ada = True

if not ada:
    print('ERROR!')