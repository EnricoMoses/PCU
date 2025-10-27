n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

min_selisih = a[-1] - a[0]
for i in range(m - n+1):
    selisih = a[i+n-1] - a[i]
    if selisih < min_selisih:
        min_selisih = selisih

print(min_selisih)

