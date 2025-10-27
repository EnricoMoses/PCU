while True:
    x = int(input())
    if 0 < x <= 1_000_000:
        break

counter = 0
while x > 0:
    counter += 1
    if x % 2 == 0:
        x = x - 99
    else:
        x = x + 3

print(counter)