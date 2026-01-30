n = int(input())
j1 = int(input())
j2 = int(input())

bisa = False
for i in range(j1 + 1):
    for j in range(j2 + 1):
        for k in range(j3 + 1):
            if i * 1 + j * 2 + k * 3 == n:
                print(i, j, k)
                bisa = True

if not bisa:
    print('TIDAK BISA')


