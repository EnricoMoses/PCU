while True:
    bumi, mars = map(int, input().split())

    if 0 <= bumi <= 364 and 0 <= mars <= 686:
        break

d = (365 - bumi) % 365

while (mars + d) % 687 != 0:
    d += 365
print(d)