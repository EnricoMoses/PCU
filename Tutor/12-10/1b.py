n, j1, j2, j3 = map(int, input().split())

found = False

for x1 in range(j1 + 1):
    for x2 in range(j2 + 1):
        for x3 in range(j3 + 1):
            if x1*1 + x2*2 + x3*3 == n:
                print(f"{x1} {x2} {x3}")
                found = True

if not found:
    print("TIDAK BISA")