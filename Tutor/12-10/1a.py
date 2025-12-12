n = int(input())

pieces = [3, 2, 1]
count = 0
for p in pieces:
    count += n // p
    n %= p

print(count)
