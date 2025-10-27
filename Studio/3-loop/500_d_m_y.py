d = int(input())
m = int(input())
y = int(input())

for _ in range(500):
    d += 1

    if m == 2:
        if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0):
            max_day = 29
        else:
            max_day = 28

    elif m in [1,3,5,7,9,10,12]:
        max_day = 31

    else:
        max_day = 30


    if d > max_day:
        d = 1
        m += 1
        if m > 12:
            m = 1
            y += 1

print(f'{d} {m} {y}')