n, m = map(int, input().split())
sneezes = 0

for _ in range(n):
    if m % 2 == 1:
        sneezes += 1
    m //= 2

print(sneezes)