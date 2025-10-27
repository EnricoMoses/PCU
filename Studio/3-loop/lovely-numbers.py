n = int(input())

isPrima = True
if n < 2:
    isPrima = False
else:
    for i in range(2, n):
        if n % i == 0:
            isPrima = False

if isPrima and (n % 10 == 3 or n // 10 == 3):
    print('YES')
else:
    print('NO')