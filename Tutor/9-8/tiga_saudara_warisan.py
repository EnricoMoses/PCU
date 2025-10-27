a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print('Semua adil')
elif a == b or a == c or b == c:
    print('Dua setara')
else :
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a
    print(a, b, c)

