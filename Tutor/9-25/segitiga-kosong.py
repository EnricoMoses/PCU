n = 4

for i in range(n):
    for j in range(n-1-i):
        print(' ', end='')

    for j in range(i+1):
        if j == 0 or j == i:
            print('*', end=' ')
        else:
            print(' ', end=' ')

    print()

# for i in range(n):
#     print('*', end=' ')

for i in range(1, n):
    for j in range(i):
        print(' ', end='')

    for j in range(n-1):
        if j == 0 or j == n-i-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')

    print()