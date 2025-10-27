n = int(input('How tall is yout tree? '))

max_L = 2*n - 1
for k in range(1, n+1):
    stars = 2 * k - 1
    print(' ' * ((max_L - stars) // 2) + '*' * stars)

for _ in range(n -1):
    for k in range(2, n+1):
        stars = 2 * k - 1
        print(' ' * ((max_L - stars) // 2) + '*' * stars)

for _ in range(n):
    print(' ' * ((max_L - 1) // 2) + '*')

print('~~Merry Christmas~~')
