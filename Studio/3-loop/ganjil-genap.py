n = int(input())

if n % 2 == 0:
    for i in range(n):
        print(i*2, end=' ')
else:
    for i in range(1, n+1):
        print(i*2-1, end=' ')