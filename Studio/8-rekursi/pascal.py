def comb(n,k):
    if k == 0 or k == n:
        return 1
    return comb(n - 1, k - 1) + comb(n - 1, k)

def build_row(r, k=0):
    if k > r:
        return []
    return [comb(r, k)] + build_row(r, k + 1)

def print_pascal(n, r=0):
    if r == n:
        return
    row = build_row(r)
    print(' '.join(map(str, row)))
    print_pascal(n, r + 1)

n = int(input())
print_pascal(n)
