n = int(input())

for brs in range(n, 0, -1):
    for kol in range(brs):
        print(kol + 1, end=' ')
    print()