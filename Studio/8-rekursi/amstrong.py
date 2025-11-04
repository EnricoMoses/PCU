def amstrong_sum(x, k):
    if x == 0:
        return 0
    return (x % 10) ** k + amstrong_sum(x // 10, k)


n = int(input())
k = len(str(abs(n)))

total = amstrong_sum(abs(n), k)

if total == n:
    print(f'{n} adalah bilangan Armstrong.')
else:
    print(f'{n} bukan bilangan Armstrong.')