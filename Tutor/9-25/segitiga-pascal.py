import math

n = 4
for i in range(n):
    for j in range(n-1-i):
        print(' ', end='')

    for j in range(i+1):
        # print('*', end=' ')
        x = math.factorial(i) // (math.factorial(i - j) * math.factorial(j))
        print(x, end=' ')

    print()