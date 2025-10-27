n = int(input())

for i in range(1, n):
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


