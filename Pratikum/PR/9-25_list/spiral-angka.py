n = int(input())

spiral = [0] * (n*n)

num = 1

top, bottom = 0, n - 1
left, right = 0, n - 1

while left <= right and top <= bottom:
    # kiri -> kanan (baris top)
    for c in range(left, right + 1):
        idx = top * n + c
        spiral[idx] = num
        num += 1
    top += 1

    for r in range(top, bottom + 1):
        idx = r * n + right
        spiral[idx] = num
        num += 1
    right -= 1

    if top <= bottom:
        for c in range(right, left - 1, -1):
            idx = bottom * n + c
            spiral[idx] = num
            num += 1
        bottom -= 1

    if left <= right:
        for r in range(bottom, top - 1, -1):
            idx = r * n + left
            spiral[idx] = num
            num += 1
        left += 1


for r in range(n):
    row = []
    for c in range(n):
        row.append(str(spiral[r * n + c]))
    print(' '.join(f'{x:>2}' for x in row))

