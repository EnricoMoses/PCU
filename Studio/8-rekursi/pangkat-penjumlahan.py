X = int(input())
N = int(input())

def count_ways(x, n, start):
    p = start ** n
    if p == x:
        return 1
    if p > x:
        return 0
    return count_ways(x - p, n, start + 1) + count_ways(x, n, start + 1)

print(count_ways(X, N, 1))