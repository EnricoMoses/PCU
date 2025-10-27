while True:
    n = int(input())
    if 0 < n < 3000 :
        break

if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print('true')
else :
    print('false')