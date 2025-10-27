x = int(input())

a = 0
for n in range(1, 51):
    a += (x + n)

    value = a % 10
    print(value, end=' ')
    if n % 5 == 0:
        print()