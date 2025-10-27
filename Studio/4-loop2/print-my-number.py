awal = int(input())
akhir = int(input())

ada = False
for i in range(awal, akhir + 1):
    # print(i)
    prima = True
    if i < 2:
        prima = False
    else:
        for j in range(2, i):
            if i % j == 0:
                prima = False
                break

    if prima:
        print(i, end=' ')
        ada = True
if not ada:
    print('ERROR!')